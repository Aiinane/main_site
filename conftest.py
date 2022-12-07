import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By





# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default= None,
#                      help="Choose browser: chrome or firefox")

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)                    

#@pytest.mark.parametrize('language', ["en"])
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        # options = Options()
        # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        # fp = webdriver.FirefoxProfile()
        # fp.set_preference("intl.accept_languages", 'en')
        # browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture
# def go_to_main_page():
#     link = "https://nextua.transportica.com/uk/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open() 
#     time.sleep(10)
    

    

#Теперь, сколько бы файлов с тестами мы ни создали, 
# у тестов будет доступ к фикстуре browser. Фикстура передается 
# в тестовый метод в качестве аргумента. Таким образом можно удобно
#  переиспользовать одни и те же вспомогательные функции в разных частях проекта.
# ОЧЕНЬ ВАЖНО! 
# Есть одна важная особенность поведения конфигурационных файлов,
#  о которой вы обязательно должны знать. PyTest автоматически находит и подгружает
#  файлы conftest.py, которые находятся в директории с тестами. Если вы храните все свои 
# скрипты для курса в одной директории, будьте аккуратны и следите, чтобы не возникало ситуации,
#  когда вы запускаете тесты из папки tests:

