import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene.support.shared import browser


@pytest.fixture(
    autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)


browser.quit()
