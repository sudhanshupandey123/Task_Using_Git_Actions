from playwright.sync_api import sync_playwright

p = sync_playwright().start()


def before_scenario(context, scenario):
    context.browser = p.firefox.launch(headless=True, slow_mo=5000)
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    context.page.close()
    context.browser.close()
