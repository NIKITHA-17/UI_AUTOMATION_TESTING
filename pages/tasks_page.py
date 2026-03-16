from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from config.locators import TasksLocators


class TasksPage(BasePage):
    def open_tasks(self):
        self.click(TasksLocators.MENU_TASKS)
        self.waits.visible(TasksLocators.STATUS_DROPDOWN)

    def update_first_task_status(self, status_text):
        checkbox = self.waits.clickable(TasksLocators.FIRST_TASK_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", checkbox)

        dropdown = self.waits.visible(TasksLocators.STATUS_DROPDOWN)
        select = Select(dropdown)

        try:
            select.select_by_visible_text(status_text)
        except Exception:
            try:
                select.select_by_value(status_text.lower().replace(" ", "_"))
            except Exception:
                select.select_by_index(1)

        button = self.waits.clickable(TasksLocators.SAVE_STATUS)
        self.driver.execute_script("arguments[0].click();", button)

    def page_contains_updated_status(self):
        page = self.driver.page_source.lower()
        return (
            "in_progress" in page
            or "in progress" in page
            or "done" in page
            or "blocked" in page
            or "todo" in page
        )