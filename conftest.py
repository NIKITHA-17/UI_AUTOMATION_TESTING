import pytest
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot_utils import save_screenshot
from utils.data_loader import load_test_data

logger = get_logger()

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.implicitly_wait(3)
    logger.info("Browser launched")
    yield driver
    driver.quit()
    logger.info("Browser closed")

@pytest.fixture(scope="session")
def test_data():
    return load_test_data()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            path = save_screenshot(driver, item.name)
            logger.error(f"Test failed. Screenshot saved at: {path}")