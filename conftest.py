import pytest

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.options import Options
from selene import browser, Browser, Config

from utils import attach


@pytest.fixture(
    autouse=True)  # Список всех доступных парамеров https://peter.sh/experiments/chromium-command-line-switches/
def setup_browser():
    browser.config.window_height = 1400
    browser.config.window_width = 1600
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

    browser.quit()

# @pytest.fixture(scope='function', autouse=True)
# def setup_browser():
#     browser.config.window_width = 1400
#     browser.config.window_height = 1600
#     browser.config.base_url = 'https://demoqa.com'
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": '100',
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#
#     browser.config.driver = driver
#     yield
#
#     # attach.add_screenshot(browser)
#     # attach.add_logs(browser)
#     # attach.add_html(browser)
#     # attach.add_video(browser)
#
#     browser.quit()

#
# @pytest.fixture()
# def practice_form():
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.window_width = 2000
#     browser.config.window_height = 1080
#
#     yield
#
#     browser.quit()
#
#     import pytest
#
#     from selenium import webdriver
#     from selenium.webdriver.chrome.options import Options
#     from selene import Browser, Config
#
#     from utils import attach


# @pytest.fixture(scope='function')
# def setup_browser(request):
#     browser_version = "100.0"
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#
#     browser = Browser(Config(driver))
#     yield browser
#
#     browser.quit()
