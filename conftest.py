import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def preparations():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1224
    browser.config.window_height = 1000
    browser.open('https://demoqa.com/automation-practice-form')


@pytest.fixture
def remove_advertisment():
    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')

