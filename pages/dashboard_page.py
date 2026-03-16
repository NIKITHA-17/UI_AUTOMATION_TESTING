from pages.base_page import BasePage
from config.locators import DashboardLocators


class DashboardPage(BasePage):

    def is_dashboard_loaded(self):
        return self.is_displayed(DashboardLocators.DASHBOARD_HEADER)

    def get_user_role_text(self):
        return self.text(DashboardLocators.USER_ROLE)

    def logout(self):
        self.click(DashboardLocators.LOGOUT_BTN)