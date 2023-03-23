import sys
import platform
import os
from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@fixture
def browser(context):
    chrome_options = Options()

    # Disable notifications and password manager
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Start with a blank session
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--incognito")

    # Provide the path to the Chrome WebDriver executable

    chrome_driver_path = get_chrome_driver_path()
    context.browser = Chrome(executable_path=chrome_driver_path, options=chrome_options)
    yield context.browser
    context.browser.quit()


def get_chrome_driver_path():
    system = platform.system()
    driver_file_name = None

    if system == 'Windows':
        driver_file_name = 'chromedriver.exe'
    elif system == 'Linux' or system == 'Darwin':
        driver_file_name = 'chromedriver'
    else:
        raise Exception(f'Unsupported operating system: {system}')

    return os.path.join(os.getcwd(), 'drivers', driver_file_name)


def before_all(context):
    use_fixture(browser, context)
