from playwright.sync_api import sync_playwright
import uuid
import time

out_dir = 'screenshots'

def run():
    unique = uuid.uuid4().hex[:6]
    username = f"user_{unique}"
    email = f"{username}@example.com"
    password = "SecurePass123!"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:8000/static/calculations.html')
        # register
        page.fill('#reg_username', username)
        page.fill('#reg_email', email)
        page.fill('#reg_password', password)
        page.click('#btn_register')
        page.wait_for_selector('#auth_msg')
        time.sleep(0.3)
        page.screenshot(path=f'{out_dir}/auth_registered.png')

        # create
        page.fill('#a','6')
        page.fill('#b','7')
        page.select_option('#type','multiply')
        page.click('#btn_create')
        page.wait_for_selector('#create_msg')
        time.sleep(0.3)
        page.screenshot(path=f'{out_dir}/created_calc.png')

        # list
        page.click('#btn_list')
        page.wait_for_selector('#calc_list li')
        time.sleep(0.3)
        page.screenshot(path=f'{out_dir}/list_calcs.png')

        # get first id
        items = page.query_selector_all('#calc_list li')
        if items:
            text = items[0].inner_text()
            calc_id = int(text.split()[0].lstrip('#'))
            # edit
            page.fill('#edit_id', str(calc_id))
            page.fill('#edit_a','3')
            page.fill('#edit_b','5')
            page.select_option('#edit_type','add')
            page.click('#btn_edit')
            page.wait_for_selector('#edit_msg')
            time.sleep(0.3)
            page.screenshot(path=f'{out_dir}/edited_calc.png')

            # delete
            page.fill('#edit_id', str(calc_id))
            page.click('#btn_delete')
            page.wait_for_selector('#edit_msg')
            time.sleep(0.3)
            page.screenshot(path=f'{out_dir}/deleted_calc.png')

        browser.close()

if __name__ == '__main__':
    import os
    os.makedirs('screenshots', exist_ok=True)
    run()
