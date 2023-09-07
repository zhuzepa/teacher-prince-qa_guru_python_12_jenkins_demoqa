import pytest

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100',
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
