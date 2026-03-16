from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_dashboard_role_visible(driver, test_data):
    login_page = LoginPage(driver)

    login_page.open_login()
    login_page.login_admin()

    WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()