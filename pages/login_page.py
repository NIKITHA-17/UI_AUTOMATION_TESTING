from config.settings import BASE_URL
from config.locators import LoginLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def open_login(self):
        self.open(f"{BASE_URL}/login")

    # used by other tests
    def login(self, email=None, password=None):

        if email and password:
            self.type(LoginLocators.EMAIL, email)
            self.type(LoginLocators.PASSWORD, password)

        self.click(LoginLocators.LOGIN_BTN)

    # used by auth tests
    def login_admin(self):
        self.click(LoginLocators.ADMIN_BTN)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.EMAIL)
        )

        self.click(LoginLocators.LOGIN_BTN)

    def login_user(self):
        self.click(LoginLocators.USER_BTN)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.EMAIL)
        )

        self.click(LoginLocators.LOGIN_BTN)