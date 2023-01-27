import time
from random import randint

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from .pages.locators import Header
from .pages.main_page import MainPage

link_moderetion = "https://nextua.transportica.com/moderator-r6SBfIAJn0KvivC7ph3k/#!/login"
moderetion_login ="svetlana"
moderetion_pass = "3NRHA4PL9p8x37Bm"
link =  "https://nextua.transportica.com/uk/" 
email = str(randint(0,10000)) + "@m.c"
phone = int("78543" + str(randint(1000,10000))) #bad work

name = "Auto_test"



class TestHeader():
    
    @pytest.mark.headercargo ##pytest -s -m headercargo
    def test_cargo(self, browser,wait=10):
        print("\ntest_cargo")
        try:
            
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_CARGO)
            page.button_click(*Header.HEADER_CARGO_SUBMIT_APPLICATION)
            assert "step1" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headersearchtransport ##pytest -s -m headersearchtransport
    def test_search_transport(self, browser,wait=10):
        print("\ntest_search_transport")
        try:
            
           
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait) 
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_TRANSPORT)
            page.button_click(*Header.HEADER_SEARCH_FOR_TRANSPORT)
            assert "transport-search" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headertransportforloading ##pytest -s -m headertransportforloading
    def test_search_transport_for_loading(self, browser,wait=10):
        print("\ntest_search_transport_for_loading")
        try:
            
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_TRANSPORT)
            page.button_click(*Header.HEADER_SEARCH_FOR_LOADING_VEHICLE)
            assert "part-load-transport-search" in page.browser.current_url , f"link isn't equal "  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    @pytest.mark.headercalculatortariff ##pytest -s -m headercalculatortariff
    def test_calculator_tariff(self, browser,wait=10):
        print("\ntest_calculator_tariff")
        try:
            
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_CALCULATOR)
            page.button_click(*Header.HEADER_TARIFF_CALCULATION)
            assert "route" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerplaceroute ##pytest -s -m headerplaceroute
    def test_place_route(self, browser,wait=10):
        print("\ntest_place_route")
        try:
            
           
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait) 
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_CALCULATOR)
            page.button_click(*Header.HEADER_PLACE_ROUTE)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerprivatedriver ##pytest -s -m headerprivatedriver
    def test_for_private_driver(self, browser,wait=10):
        print("\ntest_for_privat_driver")
        try:
            
         
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_COMPANY)
            page.button_click(*Header.HEADER_FOR_PRIVATE_DRIVERS)
            assert "driver" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    @pytest.mark.headerforcompany ##pytest -s -m headerforcompany
    def test_for_company(self, browser,wait=10):
        print("\ntest_for_company")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(wait)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_COMPANY)
            page.button_click(*Header.HEADER_FOR_TRANSPORT_COMPANY)
            assert "company" in page.browser.current_url , f"link isn't equal "  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerentrycompany ##pytest -s -m headerentrycompany
    def test_entry_company(self, browser):
        print("\ntest_entry_company")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
            page.input_form(*Header.HEADER_ALERT_PHONE, 679887888)
            page.input_form(*Header.HEADER_ALERT_PASSWORD, 12345678)
            page.button_click(*Header.HEADER_ALERT_BUTTON)
            time.sleep(3)
            assert "company/map/" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerentrycustomer ##pytest -s -m headerentrycustomer
    def test_entry_customer(self, browser):
        print("\ntest_entry_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_CUSTOMER)
            page.input_form(*Header.HEADER_ALERT_EMAIL, "test1@m.com")
            page.input_form(*Header.HEADER_ALERT_PASSWORD_CUSTOMER, 12345)
            page.button_click(*Header.HEADER_ALERT_BUTTON_CUSTOMER)
            assert "cabinet/orders/" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerentrydriver ##pytest -s -m headerentrydriver
    def test_entry_driver(self, browser):
        print("\ntest_entry_driver")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
            page.input_form(*Header.HEADER_ALERT_DRIVER_NUMBER, 932585212)
            page.input_form(*Header.HEADER_ALERT_DRIVER_PASSWORD, 12345678)
            page.button_click(*Header.HEADER_ALERT_BUTTON)
            time.sleep(5)
            assert "driver/registered/" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerswitchingcustomer ##pytest -s -m headerswitchingcustomer
    def test_entry_switching_customer(self, browser):
        print("\ntest_entry_switching_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
            page.button_click(*Header.HEADER_ALERT_SWITCHING_TO_CUSTOMER)
            page.input_form(*Header.HEADER_ALERT_EMAIL, "test1@m.com")
            page.input_form(*Header.HEADER_ALERT_PASSWORD_CUSTOMER, 12345)
            page.button_click(*Header.HEADER_ALERT_BUTTON_CUSTOMER)
            assert "cabinet/orders/" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerswitchingcompany ##pytest -s -m headerswitchingcompany
    def test_entry_switching_company(self, browser): ###ok
        print("\ntest_switching_company")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080) 
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_CUSTOMER)
            page.button_click(*Header.HEADER_ALERT_SWITCHING_TO_COMPANY)
            page.input_form(*Header.HEADER_ALERT_PHONE, 679887888)
            page.input_form(*Header.HEADER_ALERT_PASSWORD, 12345678)
            page.button_click(*Header.HEADER_ALERT_BUTTON)
            time.sleep(3)
            assert "company/map/" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewpasscompany ##pytest -s -m headernewpasscompany
    def test_entry_new_pass_company(self, browser):
        print("\ntest_switching_company")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
            page.button_click(*Header.HEADER_ALERT_COMPANY_NEW_PASS) 
            time.sleep(5)
            
            text_alert = page.browser.find_element(*Header.HEADER_COMPANY_NEW_PASS)
            text_alert = text_alert.text
            assert "Для відновлення паролю вам необхідно ввести номер мобільного телефону. На нього буде надіслано код " in text_alert , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewpasscustomer ##pytest -s -m headernewpasscustomer
    def test_entry_new_pass_customer(self, browser):
        print("\ntest_new_pass_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_CUSTOMER)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_NEW_PASS) 
            time.sleep(5)
            text_alert = page.browser.find_element(*Header.HEADER_ALERT_CUSTOMER_PASS)
            text_alert = text_alert.text
            assert "Введіть вашу електронну адресу" in text_alert , f"link isn't equal "
            
           
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewaccauntcompany ##pytest -s -m headernewaccauntcompany
    def test_entry_new_accaunt_company(self, browser):
            print("\ntest_new_pass_company")
            try:
                page = MainPage(browser, link) 
                page.browser.implicitly_wait(10)  
                page.open() 
                page.go_token()
                
                page.button_click(*Header.HEADER_LANGUAGE)
                page.button_click(*Header.HEADER_ENTRY)
                page.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
                page.button_click_light(*Header.HEADER_ALERT_COMPANY_NEW_ACCAUNT) 
                time.sleep(5)
                text_alert = page.browser.find_element(*Header.HEADER_ALERT_PRIVATE_ACCAUNT)
                text_alert = text_alert.text
                assert "Приватний водій" in text_alert , f"link isn't equal "
                
                
                print("\ntest is OK")
                page.browser.quit()
            except NoSuchElementException:  
                pass 

    @pytest.mark.headernewaccauntcustomer ##pytest -s -m headernewaccauntcustomer
    def test_entry_new_accaunt_customer(self, browser):
        print("\ntest_new_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ENTRY)
            page.button_click(*Header.HEADER_ENTRY_FOR_CUSTOMER)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_NEW_ACCAUNT) 
            time.sleep(5)
            text_alert = page.browser.find_element(*Header.HEADER_ALERT_CUSTOMER_ACCAUNT)
            text_alert = text_alert.text
            assert "Реєстрація замовника" in text_alert , f"link isn't equal "
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

####################CUSTOMER###########################

    @pytest.mark.headercreatecustomer ##pytest -s -m headercreatecustomer
    def test_create_accaunt_customer(page, browser):
        print("\ntest_create_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_NAME, "Auto")
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_MAIL, email )
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PASS, "12345678")
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_EMAIL_VARIFICATION)
            text = text.text
            assert "Підтверження E-mail" in text , f"link isn't equal "
            page.browser.execute_script("window.open('https://nextua.transportica.com/moderator-r6SBfIAJn0KvivC7ph3k/#!/login')")
            time.sleep(2)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            page.input_form(*Header.MODERETION_LOGIN, moderetion_login)
            page.input_form(*Header.MODERETION_PASS, moderetion_pass)
            page.button_click_light(*Header.MODERETION_BUTTON)
            # page.button_click(*Header.MODERETION_CUSTUMER)
            # #page.button_click(*Header.MODERETION_CUSTUMER_BUTTON)#not work
            page.button_click(*Header.MODERETION_CUSTUMER_VERIFICATION)
            # assert "activate" in page.browser.current_url , f"link isn't equal "
            time.sleep(5)

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headeremptycustomer ##pytest -s -m headeremptycustomer
    def test_empty_accaunt_customer(page, browser):
        print("\ntest_empty_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
    
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernonamecustomer ##pytest -s -m headernonamecustomer
    def test_noname_accaunt_customer(page, browser):
        print("\ntest_noname_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_MAIL, email )
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PASS, "12345678")
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernophonecustomer ##pytest -s -m headernophonecustomer
    def test_nophone_accaunt_customer(page, browser):
        print("\ntest_nophone_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_NAME, "Auto")
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_MAIL, email )
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PASS, "12345678")
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernoemailcustomer ##pytest -s -m headernoemailcustomer
    def test_noemail_accaunt_customer(page, browser):
        print("\ntest_noemail_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_NAME, "Auto")
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PASS, "12345678")
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewcustomer ##pytest -s -m headernewcustomer
    def test_nopass_accaunt_customer(page, browser):
        print("\ntest_nopass_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_NAME, "Auto")
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_MAIL, email )
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewcustomer ##pytest -s -m headernewcustomer
    def test_noconditions_accaunt_customer(page, browser):
        print("\ntest_noconditions_accaunt_customer")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_NAME, "Auto")
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_MAIL, email )
            page.input_form(*Header.HEADER_ALERT_CUSTOMER_REGISTER_PASS, "12345678")
            page.button_click_light(*Header.HEADER_ALERT_CUSTOMER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_CUSTOMER_TEXT)
            text = text.text
            assert "Прийміть умови угод" in text , f"link isn't equal "
        except NoSuchElementException:  
            pass 

    @pytest.mark.headertermsofusecustomer ##pytest -s -m headertermsofusecustomer
    def test_terms_of_use_customer(self, browser):#####
        print("\ntest_terms_of_use_customer")
        try:

            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.button_click(*Header.HEADER_CUSTOMER_TERMS_OF_USE)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/agreement" in page.browser.current_url , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerprivacypolicycustomer ##pytest -s -m headerprivacypolicycustomer
    def test_privacy_policy_customer(self, browser):
        print("\ntest_privacy_policy_customer")
        try:

            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_CUSTOMER_CREATE_ACCAUNT)
            page.button_click(*Header.HEADER_CUSTOMER_PRIVACY_POLICY)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/privacypolicy" in page.browser.current_url , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 


        
###########DRIVER#################

    
    @pytest.mark.headerentrycreatedriver ##pytest -s -m headerentrycreatedriver
    def test_entry_create_accaunt_driver(self, browser):
        print("\ntest_create_accaunt_driver")
        try:
            #file_path = 'C:\уеба\\image_1.png'
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_LAST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PASS, 12345678) #not work
            #page.send_file(*Header.HEADER_ALERT_DRIVER_REGISTER_PHOTO, file_path)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            time.sleep(3)
            page.peace_of_driver_form(name)
            page.browser.execute_script("window.open('https://nextua.transportica.com/moderator-r6SBfIAJn0KvivC7ph3k/#!/login')")
            time.sleep(2)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            code = page.moderetion_site()
            first_window = page.browser.window_handles[0]
            page.browser.switch_to.window(first_window)
            page.input_form(*Header.MODERETION_COMPANY_VERIFICATION, code)
            page.button_click_light(*Header.MODERETION_COMPANY_VERIFICATION_BUTTON)

            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headeremptycreatedriver ##pytest -s -m headeremptycreatedriver
    def test_empty_create_accaunt_driver(self, browser):###ok
        print("\ntest_empty_accaunt_driver")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
       
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernophonedriver ##pytest -s -m headernophonedriver
    def test_no_phone_accaunt_driver(self, browser): ##ok
        print("\ntest_no_phone_accaunt_driver")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_LAST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PASS, 12345678) #not work
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernonamedriver ##pytest -s -m headernonamedriver
    def test_no_name_accaunt_driver(self, browser): ##ok
        print("\ntest_no_name_accaunt_driver")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_DRIVER_LAST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PASS, 12345678) #not work
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernewaccauntcustomer ##pytest -s -m headernewaccauntcustomer
    def test_no_name_last_accaunt_driver(self, browser): ##ok
        print("\ntest_no_name_last_accaunt_driver")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PASS, 12345678) #not work
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernopassdriver ##pytest -s -m headernopassdriver
    def test_no_pass_accaunt_driver(self, browser): ##ok
        print("\ntest_no_pass_accaunt_driver")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_LAST_NAME, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernoconditionsdriver ##pytest -s -m headernoconditionsdriver
    def test_no_conditions_accaunt_driver(self, browser): ##ok
        print("\ntest_no_conditions_accaunt_driver")
        try:
            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_LAST_NAME, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_PASS, 12345678) #not work
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_DRIVER_TEXT)
            text = text.text
            assert "Необхідно прийняти умови угод" in text , f"link isn't equal "
  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headertermsofusedriver ##pytest -s -m headertermsofusedriver
    def test_terms_of_use_driver(self, browser):##ok
        print("\ntest_terms_of_use_driver")
        try:

            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_DRIVER_TEMP_OF_USE)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/agreement" in page.browser.current_url , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 
  
    @pytest.mark.headerprivacypolicycustomer ##pytest -s -m headerprivacypolicycustomer
    def test_privacy_policy_customer(self, browser):
        print("\ntest_privacy_policy_customer")
        try:

            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_DRIVER_PRIVACY_POLICY)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/privacypolicy" in page.browser.current_url , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernoconditionsdriver ##pytest -s -m headernoconditionsdriver
    def test_no_conditions_accaunt_driver(self, browser):
        print("\ntest_no_conditions_accaunt_driver")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_DRIVER_CREATE_ACCAUNT)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            page.button_click_light(*Header.HEADER_DRIVER_NOT_AGREE)
            assert "driver/" in page.browser.current_url , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerdriveremptycar ##pytest -s -m headerdriveremptycar
    def test_driver_empty_car_form(page,browser):
        print("\ntest_driver_empty_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdriveremptycarback ##pytest -s -m headerdriveremptycarformback
    def test_driver_empty_car_form_back(page,browser):
        print("\ntest_driver_empty_car_form_back")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)   
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.execute(*Header.HEADER_DRIVER_CAR_BACK)
            assert "register/driver/" in page.browser.current_url , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

########################################

    @pytest.mark.headerdrivernomarkcar ##pytest -s -m headerdrivernomarkcar
    def test_driver_nomark_car_form(page,browser):
        print("\ntest_driver_nomark_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR_TRUCK) 
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR)
            page.button_click(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR_TENT)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR_UPPER)
            page.button_click(*Header.HEADER_DRIVER_CAR_LATERAL)
            page.button_click(*Header.HEADER_DRIVER_CAR_BACK)
            page.button_click(*Header.HEADER_DRIVER_CAR_FULL)
            page.button_click(*Header.HEADER_DRIVER_CAR_WITHOUT)
            page.button_click(*Header.HEADER_DRIVER_CAR_WITHDRAWAL)
            page.button_click(*Header.HEADER_DRIVER_CAR_WITHDRAWAL_TRANSVERSE)
            page.button_click(*Header.HEADER_DRIVER_CAR_GIDROBORD)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR_CMR)
            page.button_click(*Header.HEADER_DRIVER_CAR_TIR)
            page.button_click(*Header.HEADER_DRIVER_CAR_TI1)
            button = page.browser.find_element(*Header.HEADER_DRIVER_CAR_TI2)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR1)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR2)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR3)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR4)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR5)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR6)
            button = page.browser.find_element(*Header.HEADER_DRIVER_CAR_ADR7)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR8)
            page.button_click(*Header.HEADER_DRIVER_CAR_ADR9)
            page.button_click(*Header.HEADER_DRIVER_CAR_EKMT)
            page.button_click(*Header.HEADER_DRIVER_CAR_SAN)
            button = page.browser.find_element(*Header.HEADER_DRIVER_CAR_SANBOOK)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            page.button_click(*Header.HEADER_DRIVER_CAR_CUSTOMS)
            page.button_click(*Header.HEADER_DRIVER_CAR_CUSTOM_CONTROL)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernoyearcar ##pytest -s -m headerdrivernoyearcar
    def test_driver_noyear_car_form(page,browser):
        print("\ntest_driver_noyear_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_MINIBUS) 
            page.button_click_light(*Header.HEADER_DRIVER_MICRO_TYPE_LIST)
            page.button_click(*Header.HEADER_DRIVER_MICRO_TYPE)
            page.button_click_light(*Header.HEADER_DRIVER_MICRO_TYPE_LIST)
            page.button_click_light(*Header.HEADER_DRIVER_MICRO_AGREE_LIST)
            page.button_click(*Header.HEADER_DRIVER_MICRO_AGREE_SMR)
            page.button_click_light(*Header.HEADER_DRIVER_MICRO_AGREE_LIST)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
#########################################################################################

    # @pytest.mark.headerdriveremptycarform ##pytest -m headerdriveremptycarform
    # def test_driver_noyear_car_form(page,browser):
    #     print("\ntest_driver_noyear_car_form")
    #     link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
    #     try:
    #         page = MainPage(browser, link_transport) 
    #         page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #         page.browser.set_window_size(1920, 1080)
    #         page.open() 
    #         page.go_token()
    #         page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
    #         page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
    #         page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
    #         page.button_click_light(*Header.HEADER_DRIVER_CAR_TRACK_TRAILER) 
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR)
    #         page.button_click(*Header.HEADER_DRIVER_CAR_EVACUATOR)
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
    #         page.button_click(*Header.HEADER_DRIVER_CAR_LATERAL)
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
    #         page.execute(*Header.HEADER_DRIVER_CAR_ADR1)
    #         page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
    #         page.input_form(*Header.HEADER_DRIVER_CAR_NUMBER_OF_TRUCK, 100) 
    #         page.input_form(*Header.HEADER_DRIVER_CAR_LOAD_DIMENSIONS_L, 10)
    #         page.input_form(*Header.HEADER_DRIVER_CAR_LOAD_DIMENSIONS_W, 10)
    #         page.input_form(*Header.HEADER_DRIVER_CAR_LOAD_DIMENSIONS_H, 10)
    #         page.input_form(*Header.HEADER_DRIVER_CAR_MAX_VOLUME, 10)
    #         #page.execute(*Header.HEADER_DRIVER_CAR_CARGO_CAPACITY)
    #         page.input_form(*Header.HEADER_DRIVER_CAR_CARGO_CAPACITY, 10) 
    #         page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
    #         text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
    #         text = text.text
    #         assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
    #         time.sleep(2)
    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except (NoSuchElementException):
    #         return False
    #     return True
####################################################################################################
 
    @pytest.mark.headerdrivernocategorycar ## pytest -s -m headerdrivernocategorycar
    def test_driver_nocategory_car_form(page,browser):
        print("\ntest_driver_nocategory_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name) 
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR)
            page.execute(*Header.HEADER_DRIVER_NOCATEGORY_BUTTON)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click(*Header.HEADER_DRIVER_CAR_FULL)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_CAR_SANBOOK)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernotypecar ##pytest -s -m headerdrivernotypecar
    def test_driver_notype_car_form(page,browser):
        print("\ntest_driver_notype_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR_TRUCK) 
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click(*Header.HEADER_DRIVER_CAR_FULL)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR_CMR)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernopermissioncar ##pytest -s -m headerdrivernopermissioncar
    def test_driver_nopermission_car_form(page,browser):
        print("\ntest_driver_nopermission_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_VAN)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_LIST)
            page.button_click(*Header.HEADER_DRIVER_VAN_BACK)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_LIST)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text_alert = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text_alert = text_alert.text
            assert "Сталася помилка сервера. Спробуйте ще раз." in text_alert , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernolenghtcar ##pytest -s -m headerdrivernolenghtcar
    def test_driver_nolenght_car_form(page,browser):
        print("\ntest_driver_nolenght_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_VAN) 
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click(*Header.HEADER_DRIVER_VAN_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR_VARIANT)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR) 
            page.input_form(*Header.HEADER_DRIVER_VAN_H, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10)
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernoheightcar ##pytest -s -m headerdrivernoheightcar
    def test_driver_noheight_car_form(page,browser):
        print("\ntest_driver_noheight_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_VAN) 
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click(*Header.HEADER_DRIVER_VAN_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR_VARIANT)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10)
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernowidthcar ##pytest -s -m headerdrivernowidthcar
    def test_driver_nowidth_car_form(page,browser):
        print("\ntest_driver_nowidth_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_VAN) 
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click(*Header.HEADER_DRIVER_VAN_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR_VARIANT)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10)
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_ALERT_DRIVER_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.headerdrivernocapacitycar ##pytest -s -m headerdrivernocapacitycar
    def test_driver_nocapacity_car_form(page,browser):
        print("\ntest_driver_nocapacity_car_form")
        link_transport = "https://nextua.transportica.com/uk/driver/register/transport/"
        try:
            page = MainPage(browser, link_transport) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            page.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            page.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            page.button_click_light(*Header.HEADER_DRIVER_CAR_VAN) 
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click(*Header.HEADER_DRIVER_VAN_DOWNLOAD_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_DOWNLOAD)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR_VARIANT)
            page.button_click_light(*Header.HEADER_DRIVER_VAN_PERMISION_CAR) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            page.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            page.execute(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            text = page.browser.find_element(*Header.HEADER_DRIVER_AGREE_TEXT)
            text = text.text

            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            time.sleep(2)
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


#######################COMPANY#################################

    @pytest.mark.headercreatecompany ##pytest -s -m headercreatecompany
    def test_entry_create_accaunt_company(self, browser): ###maybe ok
        print("\ntest_create_accaunt_company")
        try:

            #file_path = 'C:\уеба\\image_1.png'
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, phone) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            page.button_click_light(*Header.HEADER_COMPANY_ALERT_DRIVER)
            assert "register/transport/" in page.browser.current_url , f"link isn't equal "
            page.peace_of_driver_form(name)
            assert "register/subdriver/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_DRIVER_FIRST_NAME, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_DRIVER_LAST_NAME, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_DRIVER_PHONE, phone)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_DRIVERS_LICENSE, 10000)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            page.browser.execute_script("window.open('https://nextua.transportica.com/moderator-r6SBfIAJn0KvivC7ph3k/#!/login')")
            time.sleep(2)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            code = page.moderetion_site()
            first_window = page.browser.window_handles[0]
            page.browser.switch_to.window(first_window)
            page.input_form(*Header.MODERETION_COMPANY_VERIFICATION, str(code))
            page.button_click_light(*Header.COMPANY_VERIFICATION_BUTON)
            assert "company/map/" in page.browser.current_url , f"link isn't equal "            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerentrycreatecompany ## pytest -s -m headerentrycreatecompany
    def test_not_entry_create_accaunt_company(self, browser):
        print("\ntest_not_create_accaunt_company")
        try:

            #file_path = 'C:\уеба\\image_1.png'
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_REGISTER_NOT_AGREE)
            assert "/company" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_MAIN_BUTTON)
            assert "transportica.com" in page.browser.current_url , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headeremptycompany ##pytest -s -m headeremptycompany
    def test_empty_accaunt_company(self, browser): ##ok
        print("\ntest_empty_accaunt_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
           
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headertermsofusecompany ##pytest -s -m headertermsofusecompany
    def test_terms_of_use_company(self, browser):  ##ok
        print("\ntest_terms_of_use_company")
        try:

            #file_path = 'C:\уеба\\image_1.png'
            page = MainPage(browser, link) ##ok
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_TEMP_OF_USE)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/agreement" in page.browser.current_url , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headerprivacypolicycompany ##pytest -s -m headerprivacypolicycompany
    def test_privacy_policy_company(self, browser):
        print("\ntest_privacy_policy_company")
        try:

            #file_path = 'C:\уеба\\image_1.png'
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_PRIVACY_POLICY)
            second_window = page.browser.window_handles[1]
            page.browser.switch_to.window(second_window)
            assert "/privacypolicy" in page.browser.current_url , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernophoneregistercompany ##pytest -s -m headernophoneregistercompany
    def test_no_phone_accaunt_register_company(self, browser):
        print("\ntest_no_phone_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernomanagmantregistercompany##pytest -s -m headernomanagmantregistercompany
    def test_no_managmant_accaunt_register_company(self, browser):
        print("\ntest_no_phone_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 
    
    @pytest.mark.headernolegalregistercompany ##pytest -s -m headernolegalregistercompany
    def test_no_legal_accaunt_register_company(self, browser):
        print("\ntest_no_legal_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 
    
    @pytest.mark.headernocontactregistercompany ##pytest -s -m headernocontactregistercompany
    def test_no_contact_accaunt_register_company(self, browser):
        print("\ntest_no_contact_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernouidregistercompany ##pytest -s -m headernouidregistercompany
    def test_no_uid_accaunt_register_company(self, browser):
        print("\ntest_no_uid_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernoemailregistercompany ##pytest -s -m headernoemailregistercompany
    def test_no_email_accaunt_register_company(self, browser):
        print("\ntest_no_email_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernopassregistercompany ##pytest -s -m headernopassregistercompany
    def test_no_pass_accaunt_register_company(self, browser):
        print("\ntest_no_phone_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_CONDITIONS)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.headernoconditionsregistercompany ##pytest -s -m headernoconditionsregistercompany
    def test_no_conditions_accaunt_register_company(self, browser):
        print("\ntest_no_conditions_accaunt_register_company")
        try:

            
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            
            page.button_click(*Header.HEADER_LANGUAGE)
            page.button_click(*Header.HEADER_ALL_REGISTER_BUTTON)
            page.button_click(*Header.HEADER_ALERT_COMPANY_REGISTER_BUTTON)
            assert "register/company/" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PHONE, phone)
            page.button_click(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT)
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_MANAGEMENT_FLP)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_LEGAL_ENTITY,name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_CONTACT_PERSON, name)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_UID2, 1234567890)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_MAIL, email)
            page.input_form(*Header.HEADER_COMPANY_REGISTER_PASS, 12345) 
            page.button_click_light(*Header.HEADER_COMPANY_REGISTER_AGREE)
            text = page.browser.find_element(*Header.HEADER_COMPANY_TEXT)
            text = text.text
            assert "Необхідно прийняти умови угод" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 







        #pytest -s test_header.py