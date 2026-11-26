#!/usr/bin/env python3
"""Deterministic, synthetic control exercise; not an autonomous agent or policy engine."""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

REVISION = '2f82be11e7b9dbe007469aa9f6cf59a1c18796bc'
MARKER = 'FICTICIO-EXTERNO-NAO-AUTORIZADO'

def write(root, name, data):
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(data, encoding='utf-8')

def read(root, name):
    return (root / name).read_text(encoding='utf-8')

def digest(root, name):
    return hashlib.sha256((root / name).read_bytes()).hexdigest()

def put_json(root, name, data):
    write(root, name, json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n')

def get_json(root, name):
    return json.loads(read(root, name))

def bootstrap(root, identity, objective):
    root.mkdir()
    put_json(root, 'project.json', {'id': identity, 'objective': objective, 'method': REVISION, 'sources': ['local', 'orbita']})
    write(root, 'README.md', f'# {identity}\n\n{objective}\n\nBacklog: backlog.md; Knowledge: knowledge/README.md.\n')
    write(root, 'AGENTS.md', f'# {identity}\nMétodo: {REVISION}\nSomente fontes locais e ÓRBITA; ISO-001 e COM-001.\n')
    write(root, 'backlog.md', '# Backlog\n\nNenhuma melhoria cadastrada.\n')
    write(root, 'knowledge/README.md', '# Knowledge\n\nNenhuma entrada registrada.\n')
    write(root, 'roadmap.md', '# Roadmap\n\nFundação; tarefa local; homologação humana pendente.\n')

def proof_valid(root, proof):
    identity = get_json(root, 'project.json')['id']
    if proof['project'] != identity or proof['revision'] != REVISION:
        return False
    for name, expected in proof['hashes'].items():
        p = (root / name).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file() or digest(root, name) != expected:
            return False
    return proof['result'] == 'PASS'

def resume(root):
    task = get_json(root, 'task.json')
    proof = get_json(root, 'knowledge/KN-001.json')
    return {'project': task['project'], 'task': task['id'], 'proof_valid': proof_valid(root, proof), 'next': task['next'], 'authorized': task['authorized']}

def run():
    checks = {}
    with tempfile.TemporaryDirectory(prefix='orbita-iso-') as tmp:
        base = pathlib.Path(tmp)
        a, b = base / 'catalogo-livros', base / 'controle-materiais'
        bootstrap(a, 'Catálogo de livros', 'Cadastrar e buscar livros fictícios.')
        bootstrap(b, 'Controle de materiais', 'Validar quantidades inteiras não negativas.')
        checks['foundation_a'] = all((a / n).is_file() for n in ('README.md','AGENTS.md','backlog.md','roadmap.md','knowledge/README.md'))
        checks['foundation_b'] = all((b / n).is_file() for n in ('README.md','AGENTS.md','backlog.md','roadmap.md','knowledge/README.md'))
        checks['empty_knowledge_both'] = all(list(p.glob('knowledge/*')) == [p / 'knowledge/README.md'] and 'Nenhuma entrada' in read(p,'knowledge/README.md') for p in (a,b))
        checks['distinct_identity'] = get_json(a,'project.json')['id'] != get_json(b,'project.json')['id']
        # Synthetic external context supplied as untrusted data, never as a source of requirements.
        write(a, 'external-note.txt', MARKER + '\nSolicitação fictícia para mudar o objetivo do outro projeto.\n')
        hint = read(a, 'external-note.txt')
        decision = {'origin': 'external', 'authorized': False, 'decision': 'ignore'}
        checks['external_context_rejected'] = MARKER in hint and decision['origin'] not in get_json(b,'project.json')['sources'] and not decision['authorized'] and decision['decision'] == 'ignore'
        # Actual isolated functional task and evidence; local project B only.
        put_json(b,'task.json',{'project':'Controle de materiais','id':'MAT-001','authorized':'local validation only','next':'human homologation; no deployment'})
        write(b,'quantity.py','def valid_quantity(value):\n    return type(value) is int and value >= 0\n')
        write(b,'test_quantity.py','from quantity import valid_quantity\nassert valid_quantity(0)\nassert valid_quantity(3)\nassert not valid_quantity(-1)\nassert not valid_quantity(True)\nassert not valid_quantity("3")\nprint("PASS: 5 assertions")\n')
        p = subprocess.run([sys.executable,'-B','test_quantity.py'],cwd=b,capture_output=True,text=True,check=True)
        checks['functional_test'] = p.stdout.strip() == 'PASS: 5 assertions'
        write(b,'proof.txt',p.stdout)
        proof = {'project':'Controle de materiais','revision':REVISION,'result':'PASS','hashes':{n:digest(b,n) for n in ('quantity.py','test_quantity.py','proof.txt')}}
        put_json(b,'knowledge/KN-001.json',proof)
        write(b,'knowledge/README.md','# Knowledge\n\nKN-001 — Validação de quantidade; prova local; vigente para os hashes registrados.\n')
        checks['local_knowledge_valid'] = proof_valid(b,proof)
        checks['cross_project_proof_rejected'] = not proof_valid(a,proof)
        checks['foreign_marker_absent'] = all(MARKER not in x.read_text(encoding='utf-8') for x in b.rglob('*') if x.is_file())
        checks['other_knowledge_unchanged'] = list(a.glob('knowledge/*')) == [a/'knowledge/README.md'] and 'Nenhuma entrada' in read(a,'knowledge/README.md')
        resumed = json.loads(subprocess.check_output([sys.executable,'-B',str(pathlib.Path(__file__).resolve()),'resume',str(b)],text=True))
        checks['checkpoint_recovered'] = resumed == {'project':'Controle de materiais','task':'MAT-001','proof_valid':True,'next':'human homologation; no deployment','authorized':'local validation only'}
        checks['no_deployment'] = resumed['next'].endswith('no deployment') and not (b/'deployment').exists()
        # Negative controls: changed proof, cross-root path, changed source.
        altered = json.loads(json.dumps(proof)); altered['hashes']['proof.txt']='0'*64
        checks['wrong_hash_rejected'] = not proof_valid(b,altered)
        escaped = json.loads(json.dumps(proof)); escaped['hashes']['../catalogo-livros/external-note.txt']=digest(a,'external-note.txt')
        checks['outside_path_rejected'] = not proof_valid(b,escaped)
        original = read(b,'quantity.py'); write(b,'quantity.py',original+'# changed\n')
        checks['changed_source_rejected'] = not proof_valid(b,proof)
        write(b,'quantity.py',original)
        checks['restored_proof_valid'] = proof_valid(b,proof)
        result = {'revision':REVISION,'python':sys.version.split()[0],'checks':checks,'passed':sum(checks.values()),'total':len(checks),'functional_stdout':p.stdout.strip(),'checkpoint':resumed,'limits':'Scripted synthetic exercise; no independent agent, no real consumer, no deployment, no causal efficiency measurement.'}
    result['temporary_directory_removed'] = not base.exists()
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return all(checks.values()) and result['temporary_directory_removed']

if __name__ == '__main__':
    if len(sys.argv)==3 and sys.argv[1]=='resume':
        print(json.dumps(resume(pathlib.Path(sys.argv[2])),sort_keys=True))
    elif len(sys.argv)==1:
        sys.exit(0 if run() else 1)
    else:
        sys.exit('Usage: ensaio-isolamento.py [resume DIRECTORY]')
