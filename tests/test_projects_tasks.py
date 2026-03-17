from time import time
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.tasks_page import TasksPage


def test_project_creation_flow(driver, test_data):
    login_page = LoginPage(driver)
    projects_page = ProjectsPage(driver)
    project = test_data["project"]

    unique_project_name = f'{project["name"]}_{int(time())}'

    login_page.open_login()
    login_page.login_admin()

    projects_page.open_projects()
    projects_page.create_project(
        unique_project_name,
        project["description"],
        project["status"]
    )
    projects_page.search_project(unique_project_name)

    assert projects_page.project_exists(unique_project_name)


def test_task_status_update(driver, test_data):
    login_page = LoginPage(driver)
    tasks_page = TasksPage(driver)
    new_status = test_data["task"]["new_status"]

    login_page.open_login()
    login_page.login_admin()

    tasks_page.open_tasks()
    tasks_page.update_first_task_status(new_status)

    assert tasks_page.page_contains_updated_status()