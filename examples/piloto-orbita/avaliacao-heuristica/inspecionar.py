#!/usr/bin/env python3
"""Execute the synthetic UI walkthrough in local Chromium, without network access."""
import json, pathlib, sys, hashlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent

def inspect(browser, name):
    page = browser.new_page(viewport={'width': 640, 'height': 320}, device_scale_factor=1)
    errors, external = [], []
    page.on('pageerror', lambda e: errors.append(str(e)))
    def route_request(route):
        if route.request.url.startswith(('http:', 'https:')):
            external.append(route.request.url); route.abort()
        else: route.continue_()
    page.route('**/*', route_request)
    path = ROOT / (name + '.html')
    page.set_content(path.read_text(encoding='utf-8'))
    initial = page.locator('#results li').all_text_contents()
    label = page.locator('#search button[type=submit], #search button:not([type])').first.inner_text()
    query = page.locator('#query')
    query.fill('vidro'); query.press('Enter')
    found = page.locator('#results li').all_text_contents()
    found_status = page.locator('#status').inner_text()
    query.fill('inexistente'); query.press('Enter')
    absent = page.locator('#results li').all_text_contents()
    empty_status = page.locator('#status').inner_text()
    page.screenshot(path=str(ROOT / (name + '-sem-resultados.png')))
    clear = page.get_by_role('button', name='Limpar busca', exact=True)
    has_clear = clear.count() == 1
    if has_clear:
        clear.click()
    else:
        query.fill(''); query.press('Enter')
    reset = page.locator('#results li').all_text_contents()
    reset_query = query.input_value()
    page.screenshot(path=str(ROOT / (name + '-lista.png')))
    checks = {'initial_three_titles':len(initial)==3,'existing_title':found==['A Ilha de Vidro'],'absent_title':absent==[],'action_label':label=='Buscar','found_feedback':'1 livro encontrado' in found_status,'empty_feedback':'Nenhum livro encontrado' in empty_status,'explicit_reset':has_clear and reset_query=='' and reset==initial,'no_page_error':not errors,'no_network_request':not external}
    result={'revision':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'observations':{'initial':initial,'search_label':label,'found':found,'found_status':found_status,'absent':absent,'empty_status':empty_status,'explicit_reset':has_clear,'reset':reset,'reset_query':reset_query,'page_errors':errors,'external_requests':external},'checks':checks,'passed':sum(checks.values()),'total':len(checks)}
    page.close(); return result

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    results=[inspect(browser,n) for n in sys.argv[1:]]
    print(json.dumps({'browser':browser.version,'results':results},ensure_ascii=False,indent=2,sort_keys=True))
    browser.close()
