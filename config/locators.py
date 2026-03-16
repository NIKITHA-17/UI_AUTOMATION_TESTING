from selenium.webdriver.common.by import By


class LoginLocators:
    ADMIN_BTN = (By.XPATH, "//button[contains(.,'Admin')]")
    USER_BTN = (By.XPATH, "//button[contains(.,'User')]")
    EMAIL = (By.XPATH, "//input[@placeholder='Enter email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter password']")
    LOGIN_BTN = (By.XPATH, "//button[contains(.,'Sign In')]")
    ERROR = (By.XPATH, "//*[contains(text(),'Invalid') or contains(text(),'required') or contains(text(),'error')]")


class DashboardLocators:
    DASHBOARD_HEADER = (By.XPATH, "//h1[contains(.,'Dashboard')]")
    USER_ROLE = (By.XPATH, "//*[contains(.,'Admin User') or contains(.,'admin')]")
    LOGOUT_BTN = (By.XPATH, "//button[contains(.,'Logout') or contains(.,'Sign Out')]")


class UsersLocators:
    MENU_USERS = (By.XPATH, "//a[contains(@href,'/users')]")
    USERS_TABLE = (By.XPATH, "//table | //h1[contains(.,'Users')] | //h2[contains(.,'Users')]")


class ProjectsLocators:
    MENU_PROJECTS = (By.XPATH, "//a[contains(@href,'/projects')]")
    PAGE_HEADER = (By.XPATH, "//h1[contains(.,'Projects')]")
    ADD_PROJECT_BTN = (By.XPATH, "//button[contains(.,'New Project')]")
    PROJECT_NAME = (By.XPATH, "(//input[not(@type='search') and not(@placeholder='Search title or description')])[1]")
    PROJECT_DESC = (By.XPATH, "(//textarea)[1]")
    PROJECT_STATUS = (By.XPATH, "(//select)[last()]")
    SAVE_PROJECT = (By.XPATH, "//button[contains(.,'Create') or contains(.,'Save')]")
    SEARCH_PROJECT = (By.XPATH, "//input[@placeholder='Search title or description']")
    PROJECT_ROW = (By.XPATH, "//table//tr")


class TasksLocators:
    MENU_TASKS = (By.XPATH, "//a[contains(@href,'/tasks')]")
    PAGE_HEADER = (By.XPATH, "//h1[contains(.,'Tasks')]")
    FIRST_TASK_CHECKBOX = (By.XPATH, "(//table//tbody//input[@type='checkbox'])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//select)[4]")
    SAVE_STATUS = (By.XPATH, "//button[contains(.,'Apply Bulk Update')]")
    FIRST_STATUS_BADGE = (By.XPATH, "(//table//tbody//tr[1]//td)[3]//*[self::span or self::div]")


class BrowserScenarioLocators:
    MENU_TEST_SCENARIOS = (By.XPATH, "//a[contains(@href,'/test-scenarios')]")
    PAGE_HEADER = (By.XPATH, "//h1[contains(.,'UI Test Scenarios')]")
    ALERT_BTN = (By.XPATH, "//button[contains(.,'Trigger Alert')]")
    CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Trigger Confirm')]")
    PROMPT_BTN = (By.XPATH, "//button[contains(.,'Trigger Prompt')]")
    RESULT_LABEL = (By.XPATH, "//*[contains(.,'Confirm result') or contains(.,'Prompt result')]")
    NEW_TAB_BTN = (By.XPATH, "//button[contains(.,'Open New Tab')]")
    POPUP_BTN = (By.XPATH, "//button[contains(.,'Open Popup Window')]")
    IFRAME = (By.XPATH, "//iframe")
    FRAME_TEXT = (By.XPATH, "//*[contains(.,'Example Domain')]")