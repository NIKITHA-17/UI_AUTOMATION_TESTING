from pages.login_page import LoginPage
from pages.users_page import UsersPage


def test_admin_users_page_access(driver, test_data):
    login_page = LoginPage(driver)
    users_page = UsersPage(driver)

    login_page.open_login()
    login_page.login_admin()

    users_page.open_users()
    assert users_page.is_users_table_visible()


def test_non_admin_access_restriction(driver, test_data):
    login_page = LoginPage(driver)

    login_page.open_login()
    login_page.login_user()

    driver.get(driver.current_url.rstrip("/") + "/users")
    page_text = driver.page_source.lower()

    assert (
        "access denied" in page_text
        or "unauthorized" in page_text
        or "login" in page_text
        or "404" in page_text
        or "page not found" in page_text
    )