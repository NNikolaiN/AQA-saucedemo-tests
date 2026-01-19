import allure
import pytest
from playwright.sync_api import sync_playwright

def pytest_runtest_makereport(item, call):
    page = item.funcargs.get("page")
    if call.when == "call" and call.excinfo is not None:
        allure.attach(page.screenshot(), name="screenshot_on_fail", attachment_type=allure.attachment_type.PNG)
        
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()