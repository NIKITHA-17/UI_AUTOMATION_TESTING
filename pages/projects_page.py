from selenium.webdriver.support.ui import Select
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

    def search_project(self, name):
        self.type(ProjectsLocators.SEARCH_PROJECT, name)

    def project_exists(self, project_name):
        rows = self.driver.find_elements(*ProjectsLocators.PROJECT_ROW)
        return any(project_name.lower() in row.text.lower() for row in rows)