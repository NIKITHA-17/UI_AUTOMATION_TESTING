from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_admin_login(driver):

    login_page = LoginPage(driver)

    login_page.open_login()
    login_page.login_admin()

    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in driver.current_url.lower()


def test_valid_user_login(driver):

    login_page = LoginPage(driver)

    login_page.open_login()
    login_page.login_user()

    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in driver.current_url.lower()