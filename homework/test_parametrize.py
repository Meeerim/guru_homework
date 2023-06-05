"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selenium import webdriver
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 1024)])
def desktop_setup(request):
    chrome_browser = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_browser
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield
    browser.quit()


@pytest.mark.parametrize("desktop_setup", [(2560,1440)], indirect=True)
def test_github_desktop(desktop_setup):
    browser.open('https://github.com')
    browser.config.timeout = 2.0
    browser.element('a.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("desktop_setup", [(360,740)], indirect=True)
def test_github_mobile(desktop_setup):
    browser.open('https://github.com')
    browser.config.timeout = 2.0
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
