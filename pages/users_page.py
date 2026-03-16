from pages.base_page import BasePage
from config.locators import UsersLocators


class UsersPage(BasePage):

    def open_users(self):
        self.click(UsersLocators.MENU_USERS)

    def is_users_table_visible(self):
        return self.is_displayed(UsersLocators.USERS_TABLE)