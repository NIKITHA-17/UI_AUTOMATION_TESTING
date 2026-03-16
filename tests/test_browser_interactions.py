from pages.login_page import LoginPage
from pages.test_scenarios_page import BrowserScenariosPage


def test_alerts_handling(driver, test_data):
    login_page = LoginPage(driver)
    test_page = BrowserScenariosPage(driver)

    login_page.open_login()
    login_page.login_admin()

    test_page.open_page()
    test_page.handle_alert()
    test_page.handle_confirm()

    assert "confirm result" in test_page.get_result_text().lower()


def test_frames_and_windows(driver, test_data):
    login_page = LoginPage(driver)
    test_page = BrowserScenariosPage(driver)

    login_page.open_login()
    login_page.login_admin()

    test_page.open_page()
    frame_text = test_page.switch_to_iframe_and_get_text()
    title, url = test_page.open_new_tab_and_validate()
    popup_title = test_page.open_popup_and_switch_back()

    assert "example domain" in frame_text.lower()
    assert title != "" or url != ""
    assert popup_title is not None