"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selenium import webdriver
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1242, 2688)])
def browser_desktop_setup(request):
    chrome_browser = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_browser
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield
    browser.quit()


def test_github_desktop(browser_desktop_setup):
    browser.open('https://github.com')
    browser.config.timeout = 2.0
    browser.element('a.HeaderMenu-link--sign-in').click()


@pytest.fixture(params=[(360, 640), (414, 896), (360, 800)])
def mobile_browser_setup(request):
    chrome_browser = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_browser
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield
    browser.quit()


def test_github_mobile(mobile_browser_setup):
    browser.open('https://github.com')
    browser.config.timeout = 2.0
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()

