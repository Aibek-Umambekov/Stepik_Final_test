import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    print(f'\nStarting browser with language: {language}...')
    browser = webdriver.Chrome()  # Измените на нужный вам драйвер
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print('\nQuitting browser...')
    browser.quit()
