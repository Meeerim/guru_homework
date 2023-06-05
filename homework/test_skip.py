"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from selene import browser
from selenium import webdriver


@pytest.fixture(params=[(1920, 1280), (1600, 1024), (1242, 2688), (828, 1792)])
def browser_setup(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    yield
    browser.quit()


def test_github_desktop(browser_setup):
    if browser.config.window_height < 1242:
        pytest.skip('Пропускаем мобильные тесты т.к соотношение сторон не подходит')
    else:
        browser.open("https://github.com/")
        browser.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_setup):
    if browser.config.window_height > 1279:
        pytest.skip("Пропускаем декстопные тесты т.к соотношение сторон не подходит")
    else:
        browser.open('https://github.com')
        browser.config.timeout = 2.0
        browser.element('.flex-column [aria-label="Toggle navigation"]').click()
        browser.element('a.HeaderMenu-link--sign-in').click()
