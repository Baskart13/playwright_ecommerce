import pytest
from playwright.sync_api import Playwright, sync_playwright
from pages.login_page import Loginpage

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser  = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()

@pytest.fixture(scope='session')
def logged_in_page(browser):
    navpage = browser.new_page()
    loginpage=Loginpage(navpage)
    loginpage.navigate()
    loginpage.login()
    yield navpage
    navpage.close()




