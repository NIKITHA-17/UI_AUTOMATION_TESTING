from utils.wait_utils import WaitUtils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = WaitUtils(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.waits.clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.waits.visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.clear()
        element.send_keys(text)

    def text(self, locator):
        return self.waits.visible(locator).text

    def is_displayed(self, locator):
        try:
            return self.waits.visible(locator).is_displayed()
        except Exception:
            return False