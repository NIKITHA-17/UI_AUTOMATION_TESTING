from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import BROWSER, HEADLESS, RUN_MODE, GRID_URL


def _chrome_options():
    options = ChromeOptions()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    return options


def get_driver():
    if RUN_MODE == "grid":
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=_chrome_options()
        )
        driver.set_window_size(1920, 1080)
        return driver

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=_chrome_options())
    driver.set_window_size(1920, 1080)
    return driver