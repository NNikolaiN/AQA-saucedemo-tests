import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.title("Успешный вход с обычным пользователем")
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Inventory page did not load correctly"
    expect(page.locator("span.title")).to_have_text("Products")


@allure.title("Вход с неверным паролем")
def test_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")
    
    error_text = login_page.get_error_message()
    assert "do not match" in error_text.lower()
    expect(page).to_have_url("https://www.saucedemo.com/")


@allure.title("Вход с заблокированным пользователем")
def test_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    
    error_text = login_page.get_error_message()
    assert "locked out" in error_text.lower()
    expect(page).to_have_url("https://www.saucedemo.com/")


@allure.title("Вход с пустыми полями - проверка валидации")
def test_field_validation(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "")
    
    error_text = login_page.get_error_message()
    assert "username is required" in error_text.lower()
    expect(page).to_have_url("https://www.saucedemo.com/")


@allure.title("Вход с медленным пользователем - обработка задержек")
def test_performance_glitch_user(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    
    login_page.login("performance_glitch_user", "secret_sauce")
    
    page.wait_for_load_state("networkidle", timeout=15000)
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Inventory page did not load correctly after delay"
    expect(page.locator("span.title")).to_have_text("Products", timeout=10000)