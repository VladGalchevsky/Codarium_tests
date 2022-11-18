import pytest
from selene.support.shared import browser

from todomvc_test.model import config


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.browser_name = config.settings.browser_name
    driver = _maybe_driver_from_settings(config.settings)
    if driver:
        browser.config.driver = driver

    yield

    if config.settings.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()


def _maybe_driver_from_settings(settings: config.Settings):
    from selenium import webdriver

    options = None
    if settings.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = settings.headless
    elif settings.browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = settings.headless

    driver = None
    if settings.remote_url:
        options.set_capability('enableVNC', settings.remote_enableVNC)
        driver = webdriver.Remote(settings.remote_url, options=options)
    else:
        if settings.browser_name == 'chrome':
            from webdriver_manager.chrome import ChromeDriverManager
            driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options
            )
        elif settings.browser_name == 'firefox':
            from webdriver_manager.firefox import GeckoDriverManager
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options
            )
    return driver
