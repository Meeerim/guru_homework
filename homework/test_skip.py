"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest

from selene import browser, be
from selenium import webdriver


@pytest.fixture(params=[(1920, 1280), (1242, 2688), (360, 640), (414, 896)],
                ids=['desktop', 'desktop', 'mobile', 'mobile'])
def browser_setup(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    if 'desktop' in request.node.name and 'mobile' in request.node.callspec.id:
        pytest.skip('Пропускаем тесты т.к соотношение сторон не подходит')
    elif 'mobile' in request.node.name and 'desktop' in request.node.callspec.id:
        pytest.skip('Пропускаем тесты т.к соотношение сторон не подходит')
    yield
    browser.quit()


def test_github_desktop(browser_setup):
    browser.open("https://github.com/")
    browser.config.timeout = 2.0
    browser.element('a.HeaderMenu-link--sign-in').should(be.visible).click()


def test_github_mobile(browser_setup):
        browser.open('https://github.com')
        browser.config.timeout = 2.0
        browser.element('.flex-column [aria-label="Toggle navigation"]').click()
        browser.element('a.HeaderMenu-link--sign-in').should(be.visible).click()
