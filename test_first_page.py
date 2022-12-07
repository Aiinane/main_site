import time
import pytest
from selenium import webdriver
from .pages.locators import Service
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class TestTheService():
    def test_try_the_service(self, browser):
        print("\ntest_try_the_service is start")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open()             
            time.sleep(5)
            page.button_click(*Service.SERVICE_BUTTON)
            assert "step1" in page.browser.current_url , f"basket isn't empty"
            print("\ntest is OK")
            page.browser.quit()  
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

    def test_leave_an_application(self, browser):
        print("\ntest_leave_an_application is start")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            time.sleep(5)

            page.button_click(*Service.APPLICATION_BUTTON)
            assert "step1" in page.browser.current_url , f"basket isn't empty"   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

    # def test_profitably(self, browser):
    #     print("\ntest_profitably is start")
    #     try:
    #         link = "https://nextua.transportica.com/uk/"
    #         page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #         page.open() 
    #         time.sleep(5)

    #         page.button_click(*Service.PROFITABLY_BUTTON)
    #         assert "route" in page.browser.current_url , f"basket isn't empty"   
    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except NoSuchElementException:  #spelling error making this code not work as expected
    #         pass

    # def test_safely(self, browser):
    #     print("\ntest_safely is start")
    #     try:
    #         link = "https://nextua.transportica.com/uk/"
    #         page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #         page.open() 
    #         time.sleep(5)

    #         page.button_click(*Service.SAFELY_BUTTON)
    #         assert "features-verified-carrier" in page.browser.current_url , f"basket isn't empty"   
    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except NoSuchElementException:  #spelling error making this code not work as expected
    #         pass

    # def test_reliably(self, browser):
    #     print("\ntest_reliably is start")
    #     try:
    #         link = "https://nextua.transportica.com/uk/"
    #         page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #         page.open() 
    #         time.sleep(5)

    #         page.button_click(*Service.RELIABLY_BUTTON)
    #         assert "features-monitoring" in page.browser.current_url , f"basket isn't empty"   
    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except NoSuchElementException:  #spelling error making this code not work as expected
    #         pass


#pytest -s test_first_page.py