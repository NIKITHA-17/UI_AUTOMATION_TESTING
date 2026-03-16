from pages.base_page import BasePage
from config.locators import BrowserScenarioLocators


class BrowserScenariosPage(BasePage):
    def open_page(self):
        self.click(BrowserScenarioLocators.MENU_TEST_SCENARIOS)
        self.waits.visible(BrowserScenarioLocators.ALERT_BTN)

    def handle_alert(self):
        self.click(BrowserScenarioLocators.ALERT_BTN)
        alert = self.waits.alert_present()
        text = alert.text
        alert.accept()
        return text

    def handle_confirm(self):
        self.click(BrowserScenarioLocators.CONFIRM_BTN)
        alert = self.waits.alert_present()
        text = alert.text
        alert.dismiss()
        return text

    def handle_prompt(self, text_value):
        self.click(BrowserScenarioLocators.PROMPT_BTN)
        alert = self.waits.alert_present()
        alert.send_keys(text_value)
        alert.accept()

    def get_result_text(self):
        return self.text(BrowserScenarioLocators.RESULT_LABEL)

    def switch_to_iframe_and_get_text(self):
        iframe = self.waits.present(BrowserScenarioLocators.IFRAME)
        self.driver.switch_to.frame(iframe)
        text = self.text(BrowserScenarioLocators.FRAME_TEXT)
        self.driver.switch_to.default_content()
        return text

    def open_new_tab_and_validate(self):
        old_handles = self.driver.window_handles
        self.click(BrowserScenarioLocators.NEW_TAB_BTN)
        self.waits.wait.until(lambda d: len(d.window_handles) > len(old_handles))
        new_handle = [h for h in self.driver.window_handles if h not in old_handles][0]
        self.driver.switch_to.window(new_handle)
        title = self.driver.title
        url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(old_handles[0])
        return title, url

    def open_popup_and_switch_back(self):
        old_handles = self.driver.window_handles
        self.click(BrowserScenarioLocators.POPUP_BTN)
        self.waits.wait.until(lambda d: len(d.window_handles) > len(old_handles))
        popup_handle = [h for h in self.driver.window_handles if h not in old_handles][0]
        self.driver.switch_to.window(popup_handle)
        popup_title = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(old_handles[0])
        return popup_title