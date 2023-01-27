from dis import findlinestarts
from random import randint
import time
import pytest
from selenium import webdriver
from .pages.locators import Company, Customers, Header, Service
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



email = str(randint(0,10000)) + "@m.c"
phone = int("78543" + str(randint(1000,10000))) 
name = "Auto_test" + str(randint(0,10000))
link = "https://nextua.transportica.com/uk/"   
   
   
   
   
class TestCustomer():
    @pytest.mark.customerneworder ##pytest -s -m customerneworder
    def test_customer_new_order(self, browser): #need to fix
        print("\ntest_customer_new_order")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_BUTTON)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW, "Рі")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_RIVNE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_CANCEL)


            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW, "Те")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_TERNOPIL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_CANCEL)

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_TENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_BACK)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)
            ##page.browser.execute_script("window.scrollTo(0, +300);")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET_EURO)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET_AGREE)
          

            
            # # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_TEMPERATURE)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            
            # # actions = ActionChains(page.browser)
            # # actions.move_by_offset(0, 50).click().perform()
            # # time.sleep(2)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TEMPERATURE)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_TEMPERATURE_INPUT, 10)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_BELTS)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_BELTS_INPUT, 10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_INPUT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_CMR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_TIR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_T1)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_T2)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR1)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR2)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR3)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR4)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR5)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR6)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR7)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR8)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_ADR9)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_EKMT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_SANPASS)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_SANBOOK)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_CUSTOMS_CERTIFICATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PERMITS_CUSTOMS_CONTROL)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WOODEN_FLOOR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_BOARD)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_COMMENTS, name)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ACCOMPANIMENT)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_ACCOMPANIMENT_PHONE, phone)####need to fix
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_ACCOMPANIMENT_NAME, name)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL_AGREE)

            
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")
            

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_VND)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_EURO)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_UAH)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CARD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASHLESS)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_UAH)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_VAT)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AT_LOADING)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AT_UNLOADING)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PREPAYMENT)
            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_PREPAYMENT_PROCENT)
            text.send_keys(Keys.BACK_SPACE)
            text.send_keys(Keys.BACK_SPACE)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PREPAYMENT_PROCENT, "1")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALERT_AGREE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)
            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ALERT_CANCEL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CANCEL_ORDER)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CANCEL_ALERT_AGREE )
            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_CANCEL_ALERT_CANCEL_TXT)
            text = text.text
            print(text)
            assert "Заявку скасовано." in text, f"need to check"
            
            


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernofrom ##pytest -s -m customernewordernofrom
    def test_customer_new_orders_no_from(self, browser):
        print("\ntest_customer_new_orders_no_from")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            time.sleep(5) 

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW, "Те")
            time.sleep(2)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_TERNOPIL)

        
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_UP)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)
            ##page.browser.execute_script("window.scrollTo(0, +300);")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_TENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET_AGREE)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME, 10)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL_AGREE)

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_VND)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_VND)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_EURO)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CARD)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASHLESS)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_VAT)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AT_LOADING)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALERT_AGREE)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernowhere ##pytest -s -m customernewordernowhere
    def test_customer_new_orders_no_where(self, browser):
        print("\ntest_customer_new_orders_no_where")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            time.sleep(5) 
            
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_FULL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_TENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PALET_AGREE)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME, 10)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ADDITIONAL_AGREE)

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            #page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

 

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_ADDITIONAL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AT_LOADING)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALERT_AGREE)
  


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernocargo ##pytest -s -m customernewordernocargo
    def test_customer_new_orders_no_cargo_name(self, browser):
        print("\ntest_customer_new_orders_no_cargo_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            #page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            #page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

 

  


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"

            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernoweight ##pytest -s -m customernewordernoweight
    def test_customer_new_orders_no_weight(self, browser):
        print("\ntest_customer_new_orders_no_weight")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            # page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            #page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

 

  


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernodownload ##pytest -s -m customernewordernodownload
    def test_company_new_orders_no_download(self, browser):
        print("\ntest_company_new_orders_no_download")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernotype ##pytest -s -m customernewordernotype
    def test_customer_new_orders_no_type(self, browser):
        print("\ntest_customer_new_orders_no_type")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            # page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            #page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernodownload ##pytest -s -m customernewordernodownload
    def test_customer_new_orders_no_download(self, browser):
        print("\ntest_customer_new_orders_no_download")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            # page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CURRENSY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            #page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordernoprise ##pytest -s -m customernewordernoprise
    def test_customer_new_orders_no_prise(self, browser):
        print("\ntest_customer_new_orders_no_prise")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            # page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")



            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text_two = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_NO_COLUMN_TXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerneworderregular ##pytest -s -m customerneworderregular
    def test_customer_new_orders_regular(self, browser):
        print("\ntest_customer_new_orders_regular")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM_DATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_MONTH)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_DATE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_AGREE)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")



            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)


            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerneworderregulareditone ##pytest -s -m customerneworderregulareditone
    def test_customer_new_orders_regular_edit_one(self, browser):
        print("\ntest_customer_new_orders_regular_edit_one")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM_DATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_MONTH)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_DATE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_SUN)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_MON)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_AGREE)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")



            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)


            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerneworderregularedittwo ##pytest -s -m customerneworderregularedittwo
    def test_customer_new_orders_regular_edit_two(self, browser):
        print("\ntest_customer_new_orders_regular_edit_two")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDAR_FROM_DATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_MONTH)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CALENDSR_TO_DATE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_SUN)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_MON)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_AGREE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_SETINGS)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_REGULAR_AGREE)
            


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")



            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)


            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerneworderback ##pytest -s -m customerneworderback
    def test_customer_new_orders_back(self, browser):
        print("\ntest_customer_new_orders_back")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_BACK)
            assert "cabinet/orders" in page.browser.current_url , f"link isn't equal "
 
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordermanysityandduble ##pytest -s -m customernewordermanysityandduble
    def test_customer_new_order_many_sity_and_duble(self, browser): #need to fix
        print("\ntest_customer_new_order_many_sity_and_duble")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_TWO, "Т")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_TERNOPIL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_FROM_THREE, "С")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_SUMI)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_FROM_FOUR, "Д")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_DNIPRO)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_FROM_FIVE, "Ч")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_NEW_CHKALOVSKE)
            
   
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_TWO, "М")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_MELITOPOL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_THREE, "П")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_PIATNUZKE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_FOUR, "В")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_VUSHENKI)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_ALL_NEW_ADD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_NEW_BUTTON)
            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE_FIVE, "П")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_PIATUHATKU)
            

            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 10)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            button = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            time.sleep(2)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_BACK)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)
            ##page.browser.execute_script("window.scrollTo(0, +300);")
            

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_PRICE_REQUEST)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_CASHLESS)


            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)
            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ALERT_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            
            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER_BAD_ALERT_TXT)
            text = text.text

            if text == "не вдалося розмістити замовлення":
                print("BUG")
            
            


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customernewordercopyinnew ##pytest -s -m customernewordercopyinnew
    def test_customer_new_orders_copy_in_new(self, browser):
        print("\ntest_customer_new_orders_copy_in_new")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ALERT_CANCEL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_COPY_IN_NEW)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerneworderagreeback ##pytest -s -m customerneworderagreeback
    def test_customer_new_orders_agree_back(self, browser):
        print("\ntest_customer_new_orders_agree_back")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_FROM, "О")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_FROM_ODESA)

            page.clear_and_write_form(*Customers.CUSTOMER_NEW_ORDER_WHERE, "Кри")
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_WHERE_KRIVUYRIG)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_CARGO, name)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_WEIGHT, 1)
            page.input_form(*Customers.CUSTOMER_NEW_ORDER_VOLUME_CARGO,10)

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE_ALL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_TYPE)
            
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_GATE)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_DOWNLOAD_TWO)


            page.input_form(*Customers.CUSTOMER_NEW_ORDER_PRISE, "17000")

            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ORDER)

            text = page.browser.find_element(*Customers.CUSTOMER_NEW_ORDER_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовлення успешно розміщено" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_ALERT_CANCEL)
            page.button_click(*Customers.CUSTOMER_NEW_ORDER_AGREE_BACK)
            assert "cabinet/orders" in page.browser.current_url , f"link isn't equal "
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    #######################    MY ORDERS  #########################################

    @pytest.mark.customermyorders ##pytest -s -m customermyorders
    def test_customer_my_orders(self, browser):
        print("\ntest_customer_my_orders")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_MY_ORDER)
            assert "cabinet/orders" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_IN_WORK)
            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK)
            text = page.browser.find_element(*Customers.CUSTOMER_MY_ORDER_END_WORK_TXT)
            text = text.text
            print(text)
            assert "Виконано" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_INFO)
            assert "cabinet/order" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_COPY_IN_NEW)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_NEW_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_MAP)
            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_MAP_BACK)


            page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_NAME_CARGO, "Auto_test9971")
            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_AGREE)
            text = page.browser.find_element(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_NAME_CARGO_TXT)
            text = text.text
            print(text)
            assert "47348" in text, f"need to check"
            page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_CLEAR)
############################# NOT WORK #################################
            # page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_FROM_CONTRY)
            # page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_FROM_CONTRY_FOCUS, "Укр")
            # page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_FROM_CONTRY_AGREE)
            # page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_FROM, "Оде")
            # page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_FROM_ODESA)
            # text = page.browser.find_element(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_NAME_CARGO_TXT)
            # text = text.text
            # print(text)
            # assert "47348" in text, f"need to check"
            # page.button_click(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_CLEAR)
            # page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_WHERE, "Кривий Ріг")
            # page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_DATE_IN, "14/01/23")
            # page.input_form(*Customers.CUSTOMER_MY_ORDER_END_WORK_FILTR_DATE_TO, "14/01/23")
########################################################################################################            
            

            page.button_click(*Customers.CUSTOMER_MY_ORDER_CANCELED)
            
            text = page.browser.find_element(*Customers.CUSTOMER_MY_ORDER_CANCELED_TXT)
            text = text.text
            print(text)
            assert "Скасовано" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_MY_ORDER_CANCELED_INFO)
            assert "cabinet/order" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_CANCELED_COPY_IN_NEW)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_NEW_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_CANCELED_MAP)
            page.button_click(*Customers.CUSTOMER_MY_ORDER_CANCELED_MAP_BACK)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER)
            
            text = page.browser.find_element(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER_TXT)
            text = text.text
            print(text)
            assert "Пошук водія" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER_INFO)
            assert "cabinet/order" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER_COPY_IN_NEW)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_MY_ORDER_BACK_NEW_ORDER)

            page.button_click(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER_MAP)
            page.button_click(*Customers.CUSTOMER_MY_ORDER_SEARCH_A_DRIVER_MAP_BACK)
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customermyroadcalculation ##pytest -s -m customermyroadcalculation
    def test_customer_road_calculation(self, browser):
        print("\ntest_customer_road_calculation ")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD)
            assert "cabinet/route" in page.browser.current_url , f"link isn't equal "

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM, "О")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ODESA)
            page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE, "К")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_KIYV)

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_TONAGE, 10)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CARD)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASH)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS_VAT)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_KM)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_TON)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE)
            time.sleep(2)
            text = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_TXT)
            text = text.text
            print(text)
            assert "477 км" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "



            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customermyroadcalculationnofor ##pytest -s -m customermyroadcalculationnofor
    def test_customer_road_calculation_no_for(self, browser):
        print("\ntest_customer_road_calculation_no_for, ENS EX")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD)
            assert "cabinet/route" in page.browser.current_url , f"link isn't equal "

            # page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM, " ")
            #page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ODESA)
            # actions = ActionChains(page.browser)
            # actions.move_by_offset(0, 300).click().perform()

            # button = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)

            page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_EMPTY_FOR, "К")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_KIYV)

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_TONAGE, 10)

   
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS)
   
            
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_TON)
           

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE)
            time.sleep(2)
            text = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_TXT)
            text = text.text
            print(text)
            assert "477 км" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "



            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customermyroadcalculationnowhere ##pytest -s -m customermyroadcalculationnowhere
    def test_customer_road_calculation_no_where(self, browser):
        print("\ntest_customer_road_calculation_no_where")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD)
            assert "cabinet/route" in page.browser.current_url , f"link isn't equal "

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM, "О")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ODESA)
            #page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE, "К")
            #page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_KIYV)

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_TONAGE, 10)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CARD)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASH)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS_VAT)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_KM)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_TON)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE)
            time.sleep(2)
            text = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_TXT)
            text = text.text
            print(text)
            assert "477 км" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "



            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customermyroadcalculationnowtonage ##pytest -s -m customermyroadcalculationnotonage
    def test_customer_road_calculation_no_tonage(self, browser):
        print("\ntest_customer_road_calculation_no_tonage END EX")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD)
            assert "cabinet/route" in page.browser.current_url , f"link isn't equal "

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM, "О")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ODESA)
            page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE, "К")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_KIYV)

            #page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_TONAGE, 10)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CARD)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASH)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CASHLESS_VAT)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_KM)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR_TON)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_GR)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE)
            time.sleep(2)
            text = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_TXT)
            text = text.text
            print(text)
            assert "477 км" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customermyroadcalculationmanycities ##pytest -s -m customermyroadcalculationmanycities
    def test_customer_road_calculation_many_cities(self, browser):
        print("\ntest_customer_road_calculation_many_cities")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD)
            assert "cabinet/route" in page.browser.current_url , f"link isn't equal "

            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM, "О")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ODESA)
            page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE, "К")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_KIYV)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ADD_NEW)
            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_NEW_ONE, "М")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_MELITOPOL)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_ADD_NEW)
            page.clear_and_write_form(*Customers.CUSTOMER_CALCULATION_ROAD_FROM_NEW_TWO, "Д")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_DNIPRO)

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_ADD_NEW)
            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_NEW_ONE, "В")
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_WHERE_VUSHENKA)
            

            button = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_TYPE_FOR_PAY)
            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_CARD)


            page.input_form(*Customers.CUSTOMER_CALCULATION_ROAD_TONAGE_FOR_SITIES, 10)

            actions = ActionChains(page.browser)
            actions.move_by_offset(0, 50).click().perform()

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_FOR_CITIES)
            time.sleep(2)
            text = page.browser.find_element(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_TXT)
            text = text.text
            print(text)
            assert "1798 км" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_CALCULATION_ROAD_AGREE_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "



            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

##################################  FEEDBACK ###############
    @pytest.mark.customerfeedback ##pytest -s -m customerfeedback
    def test_customer_feedback(self, browser):
        print("\ntest_customer_feedback")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_FEEDBACK)
            assert "cabinet/feedback" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Customers.CUSTOMER_FEEDBACK_ABOUT_MY)
            text = page.browser.find_element(*Customers.CUSTOMER_FEEDBACK_ABOUT_MY_TXT)
            text = text.text
            print(text)
            assert "Света" in text, f"need to check"

            page.button_click(*Customers.CUSTOMER_FEEDBACK_MY)

            page.button_click(*Customers.CUSTOMER_FEEDBACK_MY_EDIT)
            page.clear_and_write_form(*Customers.CUSTOMER_FEEDBACK_MY_EDIT_INPUT, "AUTO")
            page.button_click(*Customers.CUSTOMER_FEEDBACK_MY_EDIT_AGREE)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

####################   NOT  WORK ##################

    @pytest.mark.customerprofile ##pytest -s -m customerprofile
    def test_customer_profile(self, browser): ###NOT WORK
        print("\ntest_customer_profile")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE)
            assert "cabinet/profile" in page.browser.current_url , f"link isn't equal "
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_TXT)
            text = text.text
            print(text)
            assert "+38(045)678-97-65" in text, f"need to check"

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    ################################################

    @pytest.mark.customerproprofileedit ##pytest -s -m customerproprofileedit
    def test_customer_profile_edit(self, browser):### NOT WORK
        print("\ntest_customer_profile_edit")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE)
            assert "cabinet/profile" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_PROFILE_EDIT)
            page.clear_and_write_form(*Customers.CUSTOMER_PROFILE_EDIT_NAME, name)
            page.clear_and_write_form(*Customers.CUSTOMER_PROFILE_EDIT_COMPANY, name)
            page.clear_and_write_form(*Customers.CUSTOMER_PROFILE_EDIT_PHONE, phone)
            page.clear_and_write_form(*Customers.CUSTOMER_PROFILE_EDIT_PASS, 12345)

            page.button_click(*Customers.CUSTOMER_PROFILE_EDIT_SAVE)
  

            


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    
    @pytest.mark.customerprofile ##pytest -s -m customerprofile
    def test_customer_profile(self, browser): ###NOT WORK 
        print("\ntest_customer_profile")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE)
            assert "cabinet/profile" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Customers.CUSTOMER_PROFILE_SETING)
            page.button_click(*Customers.CUSTOMER_PROFILE_SETING_MAIL)
            page.button_click(*Customers.CUSTOMER_PROFILE_SETING_MESSAGE)
            page.button_click(*Customers.CUSTOMER_PROFILE_SETING_FEDDBACK)
            page.button_click(*Customers.CUSTOMER_PROFILE_SETING_SAVE)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True



    ############################## STATISTIC ##############################  NOT WORK

    @pytest.mark.customerstatisticmonth ##pytest -s -m customerstatisticmonth
    def test_customer_statistic_month(self, browser):
        print("\ntest_customer_statistic_month")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC)
            assert "cabinet/statistics/orders" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_MONTH)
            # page.button_click(*Company.COMPANY_STATISTIC_QUARTER_MONTH)
            # page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = text.text
            print(text)
            assert "51 000" in text, f"BUG"

            
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_DRIVER_TXT)
            text = text.text
            print(text)
            assert "Света" in text, f"BUG"

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_DRIVER_ORDER)
            assert "cabinet/order" in page.browser.current_url , f"link isn't equal " 


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerstatisticquarter ##pytest -s -m customerstatisticquarter
    def test_customer_statistic_quarter(self, browser): 
        print("\ntest_customer_statistic_quarter")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC)
            assert "cabinet/statistics/orders" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_QUARTER)
            # page.button_click(*Company.COMPANY_STATISTIC_QUARTER_MONTH)
            # page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = text.text
            print(text)
            assert "51 000" in text, f"BUG"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.customerstatisticyear ##pytest -s -m customerstatisticyear
    def test_customer_statistic_year(self, browser): 
        print("\ntest_customer_statistic_year")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC)
            assert "cabinet/statistics/orders" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_YEAR)
            # page.button_click(*Company.COMPANY_STATISTIC_QUARTER_MONTH)
            # page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_TONAGE)
            text = text.text
            print(text)
            assert "3" in text, f"BUG"

            
            page.button_click(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = page.browser.find_element(*Customers.CUSTOMER_PROFILE_STATISTIC_COSTS)
            text = text.text
            print(text)
            assert "51 000" in text, f"BUG"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
################################################ NOT WORK

#########################  MESSAGES ###############
 
    @pytest.mark.customermessage ##pytest -s -m customermessage
    def test_customer_message(self, browser): 
        print("\ntest_customer_message")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_MESSAGES)
            page.button_click(*Customers.CUSTOMER_MESSAGES_SETING)
            text = page.browser.find_element(*Customers.CUSTOMER_MESSAGES_SETING_TXT)
            text = text.text
            print(text)
            assert "Сповіщення на сайті" in text, f"BUG"
            page.button_click(*Customers.CUSTOMER_MESSAGES_SETING_BACK)
            text = page.browser.find_element(*Customers.CUSTOMER_MESSAGES_SETING_TXT_TWO)
            text = text.text
            print(text)
            assert "Мій профіль" in text, f"BUG"
            


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

######################## SUPORT #################

    @pytest.mark.customersupport ##pytest -s -m customersupport
    def test_customer_support(self, browser): 
        print("\ntest_customer_support")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_SUPPORT)
            text = page.browser.find_element(*Customers.CUSTOMER_SUPPORT_TXT)
            text = text.text
            print(text)
            assert "Зв'язок з оператором" in text, f"BUG"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ######################### EXIT ########################

    @pytest.mark.customerexit ##pytest -s -m customerexit
    def test_customer_exit(self, browser): 
        print("\ntest_customer_exit")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_customer()
            page.button_click(*Customers.CUSTOMER_EXIT)
            assert "nextua.transportica.com/uk" in page.browser.current_url , f"link isn't equal "

            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    #pytest -s test_customers.py