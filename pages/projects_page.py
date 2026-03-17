from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from config.locators import ProjectsLocators


class ProjectsPage(BasePage):
    def open_projects(self):
        self.click(ProjectsLocators.MENU_PROJECTS)
        self.waits.visible(ProjectsLocators.SEARCH_PROJECT)

    def create_project(self, name, description, status):
        self.click(ProjectsLocators.ADD_PROJECT_BTN)

        self.type(ProjectsLocators.PROJECT_NAME, name)
        self.type(ProjectsLocators.PROJECT_DESC, description)

        try:
            Select(self.waits.visible(ProjectsLocators.PROJECT_STATUS)).select_by_visible_text(status)
        except Exception:
            pass

        self.click(ProjectsLocators.SAVE_PROJECT)

        try:
            self.waits.invisible(ProjectsLocators.SAVE_PROJECT)
        except Exception:
            pass

    def search_project(self, name):
        box = self.waits.visible(ProjectsLocators.SEARCH_PROJECT)
        box.clear()
        box.send_keys(name)
        box.send_keys(Keys.ENTER)

    def project_exists(self, project_name):
        def _project_found(driver):
            rows = driver.find_elements(*ProjectsLocators.PROJECT_ROW)
            for row in rows:
                if project_name.lower() in row.text.lower():
                    return True
            return False

        try:
            return self.waits.wait.until(_project_found)
        except TimeoutException:
            return False