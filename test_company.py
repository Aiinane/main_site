from dis import findlinestarts
from random import randint
import time
import pytest
from selenium import webdriver
from .pages.locators import Company, Header, Service
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


class TestTheCompany():

    @pytest.mark.companymap ##pytest -s -m companymap
    def test_map_company(self, browser):
        print("\ntest_map_company")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            time.sleep(8)
            button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_COOKIE_BUTTON)   

            text = page.browser.find_element(*Company.COMPANY_ALL_CAR)
            text = text.text
            assert "Всього" in text , f"-----BUG---- "
            text = page.browser.find_element(*Company.COMPANY_FREE_CAR)
            text = text.text
            assert "Вільно" in text , f"-----BUG---- "
            text = page.browser.find_element(*Company.COMPANY_CARGO_CAR)
            text = text.text
            assert "Машин" in text , f"-----BUG---- "

      
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ################################## ORDES ################################

    @pytest.mark.companyorderalloffers ##pytest -s -m companyorderalloffers
    def test_company_order_all_offers(self, browser):
        print("\ntest_company_order_all_offers")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            text = page.browser.find_element(*Company.COMPANY_ORDERS_OFFERS)
            text = text.text
            assert "Пропозиції замовлень:" in text , f"link isn't equal " 
            page.button_click(*Company.COMPANY_ORDERS_OFFERS)
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyorderallinprocess ##pytest -s -m companyorderallinprocess
    def test_company_order_all_in_process(self, browser):
        print("\ntest_company_order_all_in_process")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.order_in_process()

    
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyorderalldone ##pytest -s -m companyorderalldone
    def test_company_order_all_done(self, browser):
        print("\ntest_company_order_all_done")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_DONE)
            # text = text.text
            # assert "Виконані:" in text , f"link isn't equal " 
            # page.button_click(*Company.COMPANY_ORDERS_DONE)
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER)
            # text = text.text
            # assert "Виконано" in text , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER) 
            # assert "driver/company/orders/order/" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER_BACK)
            page.order_done()

           

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyorderallcanceled ##pytest -s -m companyorderallcanceled
    def test_company_order_all_canceled(self, browser):#need to fix
        print("\ntest_company_order_all_canceled")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.order_cancel()
            

           

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ####################################### MY ORDERS #################################
    
    @pytest.mark.companyordermyoffersinprocess ##pytest -s -m companyordermyoffersinprocess
    def test_company_order_my_offers_in_process(self, browser):
        print("\ntest_company_order_my_offers_in_process")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_MY_ORDERS)
           
            text = page.browser.find_element(*Company.COMPANY_MY_ORDERS_IN_PROCESS)
            text = text.text
            print (text)
            number = page.browser.find_element(*Company.COMPANY_MY_ORDERS_IN_PROCESS_NUMBER)
            number = int(number.text)
            print (number)
            if number != 0:
                
                    text = page.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS_ORDER)
                    text = text.text
                    assert "В роботі" in text , f"link isn't equal "
                    page.button_click(*Company.COMPANY_ORDER) 
                    assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                    page.button_click(*Company.COMPANY_ORDER_BACK)
                    
            else:
                
                text = page.browser.find_element(*Company.COMPANY_NO_ORDERS)
                text = text.text
                assert "Замовлення, які ви розмістили самостійно\nзнаходяться на цьому екрані" in text , f"link isn't equal "

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyordermyordersdone ##pytest -s -m companyordermyordersdone
    def test_company_order_my_orders_done(self, browser):#need to fix
        print("\ntest_company_order_my_orders_done")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_MY_ORDERS)
            text = page.browser.find_element(*Company.COMPANY_MY_ORDERS_DONE)
            text = text.text 
            print(text)
            assert "Виконані:" in text , f"link isn't equal " 
            number = page.browser.find_element(*Company.COMPANY_MY_ORDERS_DONE_NUMBER)
            number = int(number.text)
            print (number)
            time.sleep(3)
            # button = page.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_ORDERS_IN_PROCESS)
            if number != 0:
                
                text = page.browser.find_element(*Company.COMPANY_MY_ORDERS_DONE_ORDER)
                text = text.text
                assert "Виконано" in text , f"link isn't equal "
                page.button_click(*Company.COMPANY_MY_ORDERS_DONE_ORDER) 
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                page.button_click(*Company.COMPANY_ORDER_BACK)
                    
            else:
                
                text = page.browser.find_element(*Company.COMPANY_MY_ORDERS_DONE)
                text = text.text
                assert "Тут знаходяться замовлення, отримані" in text , f"link isn't equal "
                
                print("\ntest is OK")
                page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyordermyofferscansel ##pytest -s -m companyordermyofferscansel
    def test_company_order_my_offers_cansel(self, browser):#need to fix
        print("\ntest_company_order_my_offers_done")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_MY_ORDERS)
            text = page.browser.find_element(*Company.COMPANY_MY_ORDERS_CENCALED)
            text = text.text
            assert "Скасовані" in text , f"link isn't equal " 
            number = page.browser.find_element(*Company.COMPANY_ORDERS_CANCELED_MY_ORDER_NUMBER)
            number = int(number.text)
            print (number)
            if number != 0:###### NEED TO FIX
                page.button_click(*Company.COMPANY_MY_ORDERS_CENCALED)
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                page.button_click(*Company.COMPANY_ORDER_BACK)
                
            else:
                page.button_click(*Company.COMPANY_MY_ORDERS_CENCALED)
                text = page.browser.find_element(*Company.COMPANY_NO_ORDERS)
                text = text.text
                assert "Замовлення, які ви розмістили самостійно\nзнаходяться на цьому екрані" in text , f"link isn't equal "
                
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER)
            # text = text.text
            # assert "Виконано" in text , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER) 
            # assert "driver/company/orders/order/" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER_BACK)

           

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    ######################################## ORDERS FOR THE DAY ##################################

    @pytest.mark.companyorderofdayinprocess ##pytest -s -m companyorderofdayinprocess
    def test_company_order_of_day_in_process(self, browser):#need to fix
        print("\ntest_company_order_my_offers_in_process")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_ORDERS_FOR_THE_DAY)
            page.order_in_process()
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS)
            # text = text.text
            # print (text)
            # number = page.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS_NUMBER)
            # number = int(number.text)
            # print (number)
            # assert "В роботі:" in text , f"link isn't equal " 
            # if number != 0:
               
            #     text = page.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS_ORDER)
            #     text = text.text
            #     assert "В роботі" in text , f"link isn't equal "
            #     page.button_click(*Company.COMPANY_ORDER) 
            #     assert "driver/company/orders/order/" in page.browser.current_url , f"link isn't equal "
            #     page.button_click(*Company.COMPANY_ORDER_BACK)
                
            # else:
                
            #     text = page.browser.find_element(*Company.COMPANY_NO_ORDERS)
            #     text = text.text
            #     assert "Тут знаходяться замовлення, отримані" in text , f"link isn't equal "


           

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyordersforthedaydone ##pytest -s -m companyordersforthedaydone
    def test_company_orders_for_the_day_done(self, browser):#need to fix
        print("\ntest_company_orders_for_the_day_done")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_ORDERS_FOR_THE_DAY)
            page.order_done()
            
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER)
            # text = text.text
            # assert "Виконано" in text , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER) 
            # assert "driver/company/orders/order/" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER_BACK)
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyordersforthedaycancel ##pytest -s -m companyordersforthedaycancel
    def test_company_orders_for_the_day_cancel(self, browser):#need to fix
        print("\ntest_company_orders_for_the_day_cancel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click (*Company.COMPANY_ORDERS_FOR_THE_DAY)
            page.order_cancel()
            
            # text = page.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER)
            # text = text.text
            # assert "Виконано" in text , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER) 
            # assert "driver/company/orders/order/" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_ORDER_BACK)

           

            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyordersforthedayoffers ##pytest -s -m companyordersforthedayoffers
    def test_company_orders_for_the_day_offers(self, browser):
        print("\ntest_company_orders_for_the_day_offers")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            
            # time.sleep(8)
            # button = page.browser.find_element(*Company.COMPANY_COOKIE_BUTTON)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_COOKIE_BUTTON)

            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click(*Company.COMPANY_ORDERS_FOR_THE_DAY)
            page.order_offers()
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    
    #################### MY NEW ORDER ####################

    @pytest.mark.companyneworderssimple ##pytest -s -m companyneworderssimple
    def test_company_new_orders_simple(self, browser):
        print("\ntest_company_new_orders_simple")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_TYPE_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_PRISE_ALERT_AGREE)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_SEE_THE_CAR)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_CAR_ALERT)
            text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CARGO_CAR_ALERT_TEXT)
            text = text.text
            assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            page.button_click(*Company.COMPANY_NEW_ORDER_CARGO_CAR_ALERT_CANCEL)
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
    @pytest.mark.companyneworderswithadress ##pytest -s -m companyneworderswithadress
    def test_company_new_orders_with_adress(self, browser):
        print("\ntest_company_new_orders_with_adress")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(3) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_ADRESS)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_ADRESS_ALERT, "Кві")
            time.sleep(3)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_ADRESS_ALERT_FIRST)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_ADRESS_ALERT_SECOND, "11")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_ADRESS_ALERT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_ADRESS)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_ADRESS_ALERT, "р")
            time.sleep(3)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_ADRESS_ALERT_FIRST)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_ADRESS_ALERT_SECOND, "11")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_ADRESS_ALERT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)
            page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            text = text.text
            assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    
    @pytest.mark.companyneworderswithadditional ##pytest -s -m companyneworderswithadditional
    def test_company_new_orders_with_additional(self, browser):
        print("\ntest_company_new_orders_with_additional")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_EURO)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
          

            
            # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_TEMPERATURE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            
            # actions = ActionChains(page.browser)
            # actions.move_by_offset(0, 50).click().perform()
            # time.sleep(2)
            
            page.button_click(*Company.COMPANY_NEW_ORDER_TEMPERATURE)
            page.input_form(*Company.COMPANY_NEW_ORDER_TEMPERATURE_INPUT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_BELTS)
            page.input_form(*Company.COMPANY_NEW_ORDER_BELTS_INPUT, 10)

            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_INPUT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CMR)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_TIR)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_T1)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_T2)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR1)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR2)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR3)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR4)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR5)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR6)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR7)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR8)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR9)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_EKMT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_SANPASS)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_SANBOOK)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CUSTOMS_CERTIFICATE)
            page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CUSTOMS_CONTROL)

            page.button_click(*Company.COMPANY_NEW_ORDER_WOODEN_FLOOR)
            page.button_click(*Company.COMPANY_NEW_ORDER_BOARD)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMMENTS, name)

            page.button_click(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT)
            page.input_form(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT_PHONE, phone)####need to fix
            page.input_form(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT_NAME, name)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # text.send_keys(Keys.BACK_SPACE)
            # text.send_keys(Keys.BACK_SPACE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            time.sleep(1)
            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_ALERT_NO_CAR)
            text_two = text_two.text
            print(text_two)
            assert "У вас немає відповідних ТЗ під дане замовлення" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnoname ##pytest -s -m companynewordersnoname
    def test_company_new_orders_no_name(self, browser):
        print("\ntest_company_new_orders_no_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
            # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_TEMPERATURE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            
            # actions = ActionChains(page.browser)
            # actions.move_by_offset(0, 50).click().perform()
            # time.sleep(2)
            
            # page.button_click(*Company.COMPANY_NEW_ORDER_TEMPERATURE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_TEMPERATURE_INPUT, 10)
            # page.button_click(*Company.COMPANY_NEW_ORDER_BELTS)
            # page.input_form(*Company.COMPANY_NEW_ORDER_BELTS_INPUT, 10)

            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_INPUT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CMR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_TIR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_T1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_T2)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR2)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR3)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR4)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR5)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR6)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR7)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR8)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_ADR9)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_EKMT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_SANPASS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_SANBOOK)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CUSTOMS_CERTIFICATE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PERMITS_CUSTOMS_CONTROL)

            # page.button_click(*Company.COMPANY_NEW_ORDER_WOODEN_FLOOR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_BOARD)
            # page.input_form(*Company.COMPANY_NEW_ORDER_COMMENTS, name)

            # page.button_click(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT)
            # page.input_form(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT_PHONE, phone)####need to fix
            # page.input_form(*Company.COMPANY_NEW_ORDER_ACCOMPANIMENT_NAME, name)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnophone ##pytest -s -m companynewordersnophone
    def test_company_new_orders_no_phone(self, browser):
        print("\ntest_company_new_orders_no_phone")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_PHONE, phone)
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnofrom ##pytest -s -m companynewordersnofrom
    def test_company_new_orders_no_from(self, browser):
        print("\ntest_company_new_orders_no_from")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            # page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            # page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT)
            # page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_NAME, name)
            # page.input_form(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_PHONE, phone)
            # page.button_click(*Company.COMPANY_NEW_ORDER_FROM_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT)
            # page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_NAME, name)
            # page.input_form(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_PHONE, phone)
            # page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_NEW_CONTACT_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


    @pytest.mark.companynewordersnowhere ##pytest -s -m companynewordersnowhere
    def test_company_new_orders_no_where(self, browser):
        print("\ntest_company_new_orders_no_where")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            # page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            # page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnocargoname ##pytest -s -m companynewordersnocargoname
    def test_company_new_orders_no_cargo_name(self, browser):
        print("\ntest_company_new_orders_no_cargo_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            #page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
    
    @pytest.mark.companynewordersnoweight ##pytest -s -m companynewordersnoweight
    def test_company_new_orders_no_weight(self, browser):
        print("\ntest_company_new_orders_no_weight")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            #page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            #page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnodownload ##pytest -s -m companynewordersnodownload
    def test_company_new_orders_no_download(self, browser):
        print("\ntest_company_new_orders_no_download")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "Луб")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY_RIVNE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "Калу")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY_LVIV)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            #page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewordersnotype ##pytest -s -m companynewordersnotype
    def test_company_new_orders_no_type(self, browser):
        print("\ntest_company_new_orders_no_type")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "Рів")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY_RIVNE)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "Льв")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY_LVIV)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)

            
          

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            #page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


    @pytest.mark.companynewordersnoprise ##pytest -s -m companynewordersnoprise
    def test_company_new_orders_no_prise(self, browser):
        print("\ntest_company_new_orders_no_prise")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_ORDERS) 
            time.sleep(5) 
            page.button_click(*Company.COMPANY_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "Мико")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY_MUKOLAIV)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "Мирго")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY_MURGOROD)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_BLIND)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)

            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_WIDTH, 10)
            page.input_form(*Company.COMPANY_NEW_ORDER_PALET_HIDHT, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_PALET_AGREE)
            page.input_form(*Company.COMPANY_NEW_ORDER_VOLUME, 10)
            page.button_click(*Company.COMPANY_NEW_ORDER_ADDITIONAL_AGREE)

            # page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            # page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)

            page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_USD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            page.button_click(*Company.COMPANY_NEW_ORDER_VND)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_EURO)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CURRENSY)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_NEW_ORDER_UAH)

            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CARD)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASHLESS)
            # page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CASH)
            # # button = page.browser.find_element(*Company.COMPANY_NEW_ORDER_UAH)
            # # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_OF_PAY)
            # page.button_click(*Company.COMPANY_NEW_ORDER_VAT)

            page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            #page.button_click(*Company.COMPANY_NEW_ORDER_AT_LOADING)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_PREPAYMENT)
            
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_PROCENT)
            # # text.send_keys(Keys.BACK_SPACE)
            # # text.send_keys(Keys.BACK_SPACE)
            # page.input_form(*Company.COMPANY_NEW_ORDER_PROCENT, "1")
   
            # time.sleep(1)
            # page.button_click(*Company.COMPANY_NEW_ORDER_PAY_MOMENT)
            # page.button_click(*Company.COMPANY_NEW_ORDER_AT_UNLOADING)


            page.button_click(*Company.COMPANY_NEW_ORDER_BUTTON_AGREE)
            # page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            # text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            # text = text.text
            # assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            # page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            text_two = page.browser.find_element(*Company.COMPANY_NEW_ORDER_AGREE_TEXT)
            text_two = text_two.text
            print(text_two)
            assert "Заповніть всі обов'язкові поля" in text_two, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    ########################## CARS ##########################

    
    # def test_company_cars(self, browser):
    #     print("\ntest_company_cars")
    #     try:
    #         page = MainPage(browser, link) 
    #         page.browser.implicitly_wait(15) 
    #         page.browser.set_window_size(1920, 1080)  
    #         page.open() 
    #         page.go_token()
    #         page.entry_to_company()
    #         page.button_click(*Company.COMPANY_CARS)
    #         assert "company/transports" in page.browser.current_url , f"link isn't equal " 
    #         page.button_click(*Company.COMPANY_CARS_CAR)
    #         assert "transports/info" in page.browser.current_url , f"link isn't equal " 
    #         page.button_click(*Company.COMPANY_CARS_CAR_BACK)
    #         assert "company/transports" in page.browser.current_url , f"link isn't equal "
    #         page.button_click(*Company.COMPANY_CARS_CAR_INFO)
    #         text = page.browser.find_element(*Company.COMPANY_CARS_CAR_ORDER)
    #         text = text.text
    #         print(text)
    #         assert "Призначити замовлення" in text, f"need to check"
    #         page.button_click(*Company.COMPANY_CARS_CAR_DRIVER)
    #         assert "company/drivers" in page.browser.current_url , f"link isn't equal "

    #         #time.sleep(5)
    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except (NoSuchElementException):
    #         return False
    #     return True

   
    @pytest.mark.companycars ##pytest -s -m companycars
    def test_company_cars(self, browser):
        print("\ntest_company_cars")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR)
            assert "transports/info" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_BACK)
            assert "company/transports" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_CARS_CAR_INFO)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_ORDER)
            text = text.text
            print(text)
            assert "Призначити замовлення" in text, f"need to check"
            page.button_click(*Company.COMPANY_CARS_CAR_DRIVER)
            assert "company/drivers" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_CARS)
            page.button_click(*Company.COMPANY_CARS_CAR_FILTER)
            page.button_click(*Company.COMPANY_CARS_CAR_ALL_CARS)
            page.button_click(*Company.COMPANY_CARS_CAR_FILTER)
            page.button_click(*Company.COMPANY_CARS_CAR_CARS_WITH_CARGO)
            page.button_click(*Company.COMPANY_CARS_CAR_FILTER)
            page.button_click(*Company.COMPANY_CARS_CAR_ENTRY_CARS)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsinfo ##pytest -s -m companycarsinfo
    def test_company_cars_info(self, browser):
        print("\ntest_company_cars_info")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR)
            assert "transports/info" in page.browser.current_url , f"link isn't equal "
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_DRIVER)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 

            ######################### NOT WORK ########################
            # page.button_click(*Company.COMPANY_CARS_CAR_DRIVER)
            # assert "drivers/info" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_CARS)
            # assert "company/transports" in page.browser.current_url , f"link isn't equal "
            ######################################################################

######################## NOT WORK#####################
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_EDIT)
            # assert "transports/transport/id" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_EDIT_BACK)
            # assert "company/transports" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_CARS_CAR)
            # assert "transports/info" in page.browser.current_url , f"link isn't equal "
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER)
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER_ALERT)
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER_ALERT_DRIVER)
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER_ALERT_AGREE)
            # text = page.browser.find_element(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER_ALERT_BAD)
            # text = text.text
            # print(text)
            # assert "Не вдалось призначити" in text, f"it's ok"
            # page.button_click(*Company.COMPANY_CARS_CAR_CAR_CHANGE_DRIVER_ALERT_BAD_AGREE)
            ###################################################################################
            
            
            page.button_click(*Company.COMPANY_CARS_CAR_CAR_DELETE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_CAR_DELETE_TEXT)
            text = text.text
            print(text)
            assert "Ви впевнені що хочете видалити машину?" in text, f"need to check"
            page.button_click(*Company.COMPANY_CARS_CAR_CAR_DELETE_ALERT_CANCEL)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ############################### NEW CAR ##############################

    @pytest.mark.companycarsnewcar ##pytest -s -m companycarsnewcar
    def test_company_cars_new_car(self, browser):
        print("\ntest_company_cars_new_car")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_TRUCK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TENT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TIR)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TIR)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_TEXT)
            text = text.text
            print(text)
            assert "Машину додано" in text, f"need to check"
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnoname ##pytest -s -m companycarsnewnoname
    def test_company_cars_new_no_name(self, browser):
        print("\ntest_company_cars_new_no_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            #page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_VAN)

            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_ISOMETR)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_VAN)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_VAN_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_VAN)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_VAN)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_VAN_CMR)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_VAN_SANBOOK)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_VAN_SANBOOK)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_VAN_BACK)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)

            


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
 
    @pytest.mark.companycarsnewnoyear ##pytest -s -m companycarsnewnoyear
    def test_company_cars_new_no_year(self, browser):
        print("\ntest_company_cars_new_no_year")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            #page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_TRACTOR)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_BLIND)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR)

            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
 
    @pytest.mark.companycarsnewnocategory ##pytest -s -m companycarsnewnocategory
    def test_company_cars_new_no_category(self, browser):
        print("\ntest_company_cars_new_no_category")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnotype ##pytest -s -m companycarsnewnotype
    def test_company_cars_new_no_type(self, browser):
        print("\ntest_company_cars_new_no_type")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnotypedownload ##pytest -s -m companycarsnewnotypedownload
    def test_company_cars_new_no_type_download(self, browser):
        print("\ntest_company_cars_new_no_type_download")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnolenght ##pytest -s -m companycarsnewnolenght
    def test_company_cars_new_no_lenght(self, browser):
        print("\ntest_company_cars_new_no_lenght")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_VOLUME, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnowidth ##pytest -s -m companycarsnewnowidth
    def test_company_cars_new_no_width(self, browser):
        print("\ntest_company_cars_new_no_width")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            #page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_VOLUME, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnoheight ##pytest -s -m companycarsnewnoheight
    def test_company_cars_new_no_height(self, browser):
        print("\ntest_company_cars_new_no_height")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_VOLUME, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewnocapacity ##pytest -s -m companycarsnewnocapacity
    def test_company_cars_new_no_capacity(self, browser):
        print("\ntest_company_cars_new_no_capacity")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 2020)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 10)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_VOLUME, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 1000)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewzero ##pytest -s -m companycarsnewzero
    def test_company_cars_new_zero(self, browser):
        print("\ntest_company_cars_new_zero")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_MARK, name)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_YEAR, 0)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_NUMBER, 1234567)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CATEGORY_MICROBUS)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_TRANSPORTER)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_UP)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_LATERAL)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_BACK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_FULL)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_NO_GATE)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_STACKS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF_TRANSVERSE)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_GIDROBORD)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_TYPE_DOWNLOAD_OFF)
            
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CMR)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_TRACTOR_T1)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_T2)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR1)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR2)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR3)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR4)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR5)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR6)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR7)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR8)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_ADR9)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_EKMT)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANBOOK)
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_SANPASS)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CONTROL)
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION_CUSTOMS_CERTIFICATE)
            # button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_TYPE)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_PERMISSION)

            page.input_form(*Company.COMPANY_CARS_CAR_NEW_LENGTH, 0)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_WIDTH, 0)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_HEIGHT, 0)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_VOLUME, 0)
            page.input_form(*Company.COMPANY_CARS_CAR_NEW_CAPACITY, 0)
            #page.button_click(*Company.COMPANY_CARS_CAR_NEW_TRAILER)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_NUMBER, 1234567)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_LENGTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_WIDTH, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_TRACTOR_HEIGHT, 10)
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_TRAILER_CAPACITY, 1000)
            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewempty ##pytest -s -m companycarsnewempty
    def test_company_cars_new_empty(self, browser):
        print("\ntest_company_cars_new_empty")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)

            button = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE)
            text = page.browser.find_element(*Company.COMPANY_CARS_CAR_NEW_SAVE_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"
            # page.input_form(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CITY, "Одеса")
            # page.button_click(*Company.COMPANY_CARS_CAR_NEW_SAVE_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycarsnewempty ##pytest -s -m companycarsnewempty
    def test_company_cars_new_empty_car(self, browser):
        print("\ntest_company_cars_new_empty_car")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CARS)
            assert "company/transports" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CAR)

            page.button_click(*Company.COMPANY_CARS_CAR_NEW_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True
        
################ DEIVER ##########################

    @pytest.mark.companydrivers ##pytest -s -m companydrivers
    def test_company_drivers(self, browser):
        print("\ntest_company_drivers")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER)
            assert "drivers/info" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_BACK)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversinfo ##pytest -s -m companydriversinfo
    def test_company_drivers_info(self, browser):
        print("\ntest_company_drivers_info")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_APPOINT_CUSTOMER)
            assert "company/add/step1" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_APPOINT_BACK)
            assert "company/orders" in page.browser.current_url , f"link isn't equal "

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversedit ##pytest -s -m companydriversedit
    def test_company_drivers_edit(self, browser):
        print("\ntest_company_drivers_edit")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_EDIT)
            assert "drivers/driver" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_EDIT_BACK)
            assert "company/drivers" in page.browser.current_url , f"link isn't equal "

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriverschangecar ##pytest -s -m companydriverschangecar
    def test_company_drivers_change_car(self, browser):
        print("\ntest_company_drivers_edit")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_CHANGE_CAR)
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_CHANGE_CAR_ALERT_TEXT)
            text = text.text
            print(text)
            assert "Назначение транспортного средства" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversfeedback ##pytest -s -m companydriversfeedback
    def test_company_drivers_feedback(self, browser):
        print("\ntest_company_drivers_feedback")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_FEEDBACK)
            assert "company/feedback" in page.browser.current_url , f"link isn't equal " 


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversinmap ##pytest -s -m companydriversinmap
    def test_company_drivers_in_map(self, browser):
        print("\ntest_company_drivers_in_map")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_INFO)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_MAP)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_MAP_CANCEL)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversfilter ##pytest -s -m companydriversfilter
    def test_company_drivers_filter(self, browser):
        print("\ntest_company_drivers_filter")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_FILTERS)
            page.button_click(*Company.COMPANY_DRIVERS_FILTERS_EMPTY)
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_FILTERS_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "Порожній" in text, f"need to check"

            page.button_click(*Company.COMPANY_DRIVERS_FILTERS)
            page.button_click(*Company.COMPANY_DRIVERS_FILTERS_WITH_CARGO)
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_FILTERS_EMPTY_TEXT)
            text = text.text
            print(text)
            assert "З вантажем" in text, f"need to check"

            page.button_click(*Company.COMPANY_DRIVERS_FILTERS)
            page.button_click(*Company.COMPANY_DRIVERS_FILTERS_ALL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


    @pytest.mark.companydriversdrivernew ##pytest -s -m companydriversdrivernew
    def test_company_drivers_driver_new(self, browser):
        print("\ntest_company_drivers_driver_new")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER_TWO)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER_TWO_NUMBER, phone)
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER_TWO_DELETE)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD_TEXT)
            text = text.text
            print(text)
            assert "Водій успішно доданий і знаходиться на перевірці" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewnophone ##pytest -s -m companydriversdrivernewnophone
    def test_company_drivers_driver_new_no_phone(self, browser):
        print("\ntest_company_drivers_driver_new_no_phone")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewnolast ##pytest -s -m companydriversdrivernewnolast
    def test_company_drivers_driver_new_no_last(self, browser):
        print("\ntest_company_drivers_driver_new_no_last")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewnofirst ##pytest -s -m companydriversdrivernewnofirst
    def test_company_drivers_driver_new_no_first(self, browser):
        print("\ntest_company_drivers_driver_new_no_first")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewnolicense ##pytest -s -m companydriversdrivernewnolicense
    def test_company_drivers_driver_new_no_license(self, browser):
        print("\ntest_company_drivers_driver_new_no_license")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            #page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewempty ##pytest -s -m companydriversdrivernewempty
    def test_company_drivers_driver_new_empty(self, browser):
        print("\ntest_company_drivers_driver_new_no_empty")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewcancel ##pytest -s -m companydriversdrivernewcancel
    def test_company_drivers_driver_new_cancel(self, browser):
        print("\ntest_company_drivers_driver_new_cancel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_CANCEL)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_CANCEL)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal "

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewbademail ##pytest -s -m companydriversdrivernewcbademail
    def test_company_drivers_driver_new_bad_email(self, browser): #need to fix
        print("\ntest_company_drivers_driver_new_bad_email")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, "email")
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewzerophone ##pytest -s -m companydriversdrivernewzerophone
    def test_company_drivers_driver_new_zero_phone(self, browser): #need to fix
        print("\ntest_company_drivers_driver_new_zero_phone")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, 0)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, 0)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewzeroname ##pytest -s -m companydriversdrivernewzeroname
    def test_company_drivers_driver_new_zero_name(self, browser): #need to fix
        print("\ntest_company_drivers_driver_new_zero_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, 0)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, name)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydriversdrivernewzerofirst ##pytest -s -m companydriversdrivernewzerofirst
    def test_company_drivers_driver_new_zero_first(self, browser): #need to fix
        print("\ntest_company_drivers_driver_new_zero_first")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_DRIVERS)
            assert "/company/drivers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, 0)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            
            text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            text = text.text
            print(text)
            assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    ################### CUSTOMERS ###################################

    @pytest.mark.companycustomers ##pytest -s -m companycustomers
    def test_company_customers(self, browser): 
        print("\ntest_company_customers")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Редактирование заказчика" in text, f"need to check"
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LAST_NAME, name)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, 0)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            # button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_CANCEL)
            
            # text = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_NO_TEXT)
            # text = text.text
            # print(text)
            # assert "Будь ласка, коректно заповніть усі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    
    @pytest.mark.companycustomerseditname ##pytest -s -m companycustomerseditname
    def test_company_customers_edit_name(self, browser): 
        print("\ntest_company_customers_edit_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Редактирование заказчика" in text, f"need to check"
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_NAME, name)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, 0)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            # button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_AGREE)
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_NAME_TXT)
            text = text.text
            print(text , name)
            assert name in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomerseditphone ##pytest -s -m companycustomerseditphone
    def test_company_customers_edit_phone(self, browser):
        print("\ntest_company_customers_edit_phone")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Редактирование заказчика" in text, f"need to check"
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_PHONE, phone)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_FIRST_NAME, 0)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            # button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_AGREE)
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_PHONE_TEXT)
            text = text.text
            new_text =   "".join(c for c in text if  c.isdecimal())
            phone_text ="380" + str(phone)
            print(new_text, phone_text)
            assert phone_text in new_text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomerseditcompany ##pytest -s -m companycustomerseditcompany
    def test_company_customers_edit_company(self, browser):
        print("\ntest_company_customers_edit_company")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Редактирование заказчика" in text, f"need to check"
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            #page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_PHONE, phone)
            page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_COMPANY, name)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_EMAIL, email)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            # button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_AGREE)
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_COMPANY_TEXT)
            text = text.text
            print(text , name)
            assert name in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomerseditemail ##pytest -s -m companycustomerseditemail
    def test_company_customers_edit_email(self, browser):
        print("\ntest_company_customers_edit_email")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Редактирование заказчика" in text, f"need to check"
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_NUMBER, phone)
            #page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_PHONE, phone)
            #page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_COMPANY, name)
            page.clear_and_write_form(*Company.COMPANY_CUSTOMERS_EDIT_EMAIL, email)
            # page.input_form(*Company.COMPANY_DRIVERS_DRIVER_NEW_LICENSE, 0)
            # button = page.browser.find_element(*Company.COMPANY_DRIVERS_DRIVER_NEW_ADD)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_AGREE)
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_EMAIL_TEXT)
            text = text.text
            print(text , email)
            assert email in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomerseditfilters ##pytest -s -m companycustomerseditfilters
    def test_company_customers_filters(self, browser):
        print("\ntest_company_customers_filters")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_ALL_CARGO)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_ALL_CARGO_TXT)
            text = text.text
            print(text)
            assert "Всього замовлень: " in text, f"need to check"
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR)
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_CENCELED)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_CENCELED_TXT)
            text = text.text
            print(text)
            assert "Нічого не знайдено" in text, f"need to check"
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR)
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_EXECUTED)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_EXECUTED_TXT)
            text = text.text
            print(text)
            assert "Виконано" in text, f"need to check"
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR)
            page.button_click(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_ALL)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_CARGO_FILTR_ALL_TXT)
            text = text.text
            print(text)
            assert "Виконано" in text, f"need to check"
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomersedineworder ##pytest -s -m companycustomersedineworder
    def test_company_customers_costomer_new_order(self, browser):
        print("\ntest_company_customers_new_order")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            # button = page.browser.find_element(*Company.COMPANY_CUSTOMERS)
            # page.browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO)
            page.button_click(*Company.COMPANY_CUSTOMERS_CUSTOMER_NEW_ORDER)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)
            page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            text = text.text
            assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)
            
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True



######################################## NEW CUSTOMER ######################

    @pytest.mark.companycustomernew ##pytest -s -m companycustomernew
    def test_company_customers_new(self, browser): 
        print("\ntest_company_customers_new")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Добавление нового заказчика" in text, f"need to check"
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_NAME, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_PHONE, phone)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_COMPANY, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_EMAIL, email)
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW_AGREE)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_NEW_AGREE_TEXT)
            text = text.text
            print(text)
            assert "Замовник успішно доданий" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomernewname ##pytest -s -m companycustomernewname
    def test_company_customers_new_no_name(self, browser): 
        print("\ntest_company_customers_new_no_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Добавление нового заказчика" in text, f"need to check"
            #page.input_form(*Company.COMPANY_CUSTOMERS_NEW_NAME, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_PHONE, phone)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_COMPANY, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_EMAIL, email)
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW_AGREE)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_NEW_NO_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomernewnamenophone ##pytest -s -m companycustomernewnamenophone
    def test_company_customers_new_no_phone(self, browser): 
        print("\ntest_company_customers_new_no_phone")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Добавление нового заказчика" in text, f"need to check"
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_NAME, name)
            #page.input_form(*Company.COMPANY_CUSTOMERS_NEW_PHONE, phone)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_COMPANY, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_EMAIL, email)
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW_AGREE)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_NEW_NO_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomernewnamenoemail ##pytest -s -m companycustomernewnamenoemail
    def test_company_customers_new_no_email(self, browser): 
        print("\ntest_company_customers_new_no_email")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW)
            page.button_click(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            text = text.text
            print(text)
            assert "Добавление нового заказчика" in text, f"need to check"
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_NAME, name)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_PHONE, phone)
            page.input_form(*Company.COMPANY_CUSTOMERS_NEW_COMPANY, name)
            #page.input_form(*Company.COMPANY_CUSTOMERS_NEW_EMAIL, email)
            page.button_click(*Company.COMPANY_CUSTOMERS_NEW_AGREE)  
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_NEW_NO_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomerdelete ##pytest -s -m companycustomerdelete
    def test_company_customers_delete(self, browser): #need to fix
        print("\ntest_company_customers_delete")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO_FOR_DELETE)
            page.button_click(*Company.COMPANY_CUSTOMERS_DELETE)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_DELETE_TXT)
            text = text.text
            print(text)
            assert "Удалить заказчика?" in text, f"need to check"
            page.button_click(*Company.COMPANY_CUSTOMERS_DELETE_CANCEL)
           


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companycustomereditdelete ##pytest -s -m companycustomereditdelete
    def test_company_customers_edit_delete(self, browser): #need to fix
        print("\ntest_company_customers_edit_delete")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_CUSTOMERS)
            assert "company/clients" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_CUSTOMERS_INFO_FOR_DELETE)
            page.button_click(*Company.COMPANY_CUSTOMERS_DELETE)
            text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_DELETE_TXT)
            text = text.text
            print(text)
            assert "Удалить заказчика?" in text, f"need to check"
            page.button_click(*Company.COMPANY_CUSTOMERS_DELETE_AGREE)
           


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    ######################### EMPLOYEE #######################

    @pytest.mark.companynewemployee ##pytest -s -m companynewemployee
    def test_company_new_employee(self, browser): #need to fix
        print("\ntest_company_employee")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_TXT)
            text = text.text
            print(text)
            assert "Приглашение успешно отправлено" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_BACK)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT_AFTER)
            text = text.text
            print(text)
            assert "Отправлено приглашение" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_CANCEL)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT_CANCEL_TXT)
            text = text.text
            print(text)
            assert "Ви підтверджуєте?" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_BUTON)

            # 
            # page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)
           


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeecancel ##pytest -s -m companynewemployeecancel
    def test_company_new_employee_cancel (self, browser): #need to fix
        print("\ntest_company_new_employee_cancel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"


            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_CANCEL_ALERT)
 
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeenew ##pytest -s -m companynewemployeenew
    def test_company_new_employee_new(self, browser): #need to fix
        print("\ntest_company_new_employee_new")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_TXT)
            text = text.text
            print(text)
            assert "Приглашение успешно отправлено" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_NEW)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_CANCEL_ALERT)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT_AFTER)
            text = text.text
            print(text)
            assert "Отправлено приглашение" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_CANCEL)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT_CANCEL_TXT)
            text = text.text
            print(text)
            assert "Ви підтверджуєте?" in text, f"need to check"
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_BUTON)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeenofirstname ##pytest -s -m companynewemployeenofirstname
    def test_company_new_employee_no_first_name(self, browser): #need to fix
        print("\ntest_company_new_employee_no_first_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            #page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_NO_IMPUT_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"
            

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeenolastname ##pytest -s -m companynewemployeenolastname
    def test_company_new_employee_no_last_name(self, browser): #need to fix
        print("\ntest_company_new_employee_no_last_name")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            #page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_NO_IMPUT_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"
            

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeenoemail ##pytest -s -m companynewemployeenoemail
    def test_company_new_employee_no_email(self, browser): #need to fix
        print("\ntest_company_new_employee_no_email")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            #page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_NO_IMPUT_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"
            

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companynewemployeezeroemail ##pytest -s -m companynewemployeezeroemail
    def test_company_new_employee_zero_email(self, browser): #need to fix
        print("\ntest_company_new_employee_zero_email")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE)
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT)
            text = text.text
            print(text)
            assert "Додавання нового співробітника" in text, f"need to check"

            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_FIRST_NAME, name)
            page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_LAST_NAME, name)
            #page.input_form(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE)

            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_NO_IMPUT_TXT)
            text = text.text
            print(text)
            assert "Ви заповнили не всі обов'язкові поля" in text, f"need to check"
            

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyemployeeedit ##pytest -s -m companyemployeeedit
    def test_company_employee_edit(self, browser): #need to fix
        print("\ntest_company_employee_edit")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_INFO)
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT)
            # text = page.browser.find_element(*Company.COMPANY_CUSTOMERS_EDIT_TEXT)
            # text = text.text
            # print(text)
            # assert "Додавання нового співробітника" in text, f"need to check"

            page.clear_and_write_form(*Company.COMPANY_EMPLOYEE_EDIT_FIRST_NAME, name)
            page.clear_and_write_form(*Company.COMPANY_EMPLOYEE_EDIT_LAST_NAME, name)
            page.clear_and_write_form(*Company.COMPANY_EMPLOYEE_EDIT_EMAIL, email)
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_AGREE)
            first_last_name = name +" "+ name
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_EDIT_FIRST_LAST_NAME_TXT )
            text = text.text
            print(text, first_last_name)
            assert first_last_name in text, f"need to check"
            text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_EDIT_EMAIL_TXT)
            text = text.text
            print(text, email)
            assert email in text, f"need to check"
            # page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_CANCEL)
            # text = page.browser.find_element(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_TXT_CANCEL_TXT)
            # text = text.text
            # print(text)
            # assert "Ви підтверджуєте?" in text, f"need to check"
            # page.button_click(*Company.COMPANY_EMPLOYEE_NEW_EMPLOYEE_AGREE_BUTON)

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyemployeeeditcancel ##pytest -s -m companyemployeeeditcancel
    def test_company_employee_edit_cancel(self, browser): #need to fix
        print("\ntest_company_employee_edit_cancel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_INFO)
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT)
            assert "manager/?managerId" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_BACK)
            assert "manager/?managerId" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_BACK_LIST)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyemployeeeditneworder ##pytest -s -m companyemployeeeditneworder
    def test_company_employee_edit_new_order(self, browser): #need to fix
        print("\ntest_company_employee_edit_new_order")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_INFO)
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.input_form(*Company.COMPANY_NEW_ORDER_NAME, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_COMPANY, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_EMAIL, email)
            page.input_form(*Company.COMPANY_NEW_ORDER_PHONE, phone)
            page.input_form(*Company.COMPANY_NEW_ORDER_FROM, "К")
            page.button_click(*Company.COMPANY_NEW_ORDER_FROM_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_WHERE, "О")
            page.button_click(*Company.COMPANY_NEW_ORDER_WHERE_CITY)
            page.input_form(*Company.COMPANY_NEW_ORDER_CARGO, name)
            page.input_form(*Company.COMPANY_NEW_ORDER_WEIGHT, 1)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_DOWNLOAD)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE_TENT)
            page.button_click(*Company.COMPANY_NEW_ORDER_TYPE)
            page.button_click(*Company.COMPANY_NEW_ORDER_PRISE)
            page.input_form(*Company.COMPANY_NEW_ORDER_PRISE_ALERT, "10000")
            page.button_click(*Company.COMPANY_NEW_ORDER_ALERT_PRISE_AGREE)
            page.button_click(*Company.COMPANY_NEW_ORDER_SEE_THE_CAR)
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT)
            text = page.browser.find_element(*Company.COMPANY_NEW_ORDER_CAR_ALERT_TEXT)
            text = text.text
            assert "ВИКАОНАВЦЯ ОБРАНО" in text , f"-----BUG---- "
            page.button_click(*Company.COMPANY_NEW_ORDER_CAR_ALERT_CANCEL)


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyemployeeeditnewordercancel ##pytest -s -m companyemployeeeditnewordercancel
    def test_company_employee_edit_new_order_cancel(self, browser): #need to fix
        print("\ntest_company_employee_edit_new_order_cancel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()
            page.button_click(*Company.COMPANY_EMPLOYEE)
            assert "/company/managers" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Company.COMPANY_EMPLOYEE_INFO)
            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_NEW_ORDER)
            assert "add/step1" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_EMPLOYEE_EDIT_NEW_ORDER_BACK)
            assert "company/orders" in page.browser.current_url , f"link isn't equal "


            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True





        ####################### DISTANCE ###############################

    @pytest.mark.companydistance ##pytest -s -m companydistance
    def test_company_distance(self, browser): #need to fix
        print("\ntest_company_distance")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_DISTANCE)
            assert "distance-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_DISTANCE_FROM, "О")
            page.input_form(*Company.COMPANY_DISTANCE_FROM, "д")
            time.sleep(2)
            page.button_click(*Company.COMPANY_DISTANCE_FROM_ODESA)
            page.input_form(*Company.COMPANY_DISTANCE_WHERE, "Е")
            page.button_click(*Company.COMPANY_DISTANCE_WHERE_ENERGODAR)

            page.button_click(*Company.COMPANY_DISTANCE_AGREE_BUTTON)

            text = page.browser.find_element(*Company.COMPANY_DISTANCE_ANSWER)
            text = text.text
            print(text)
            assert "Відстань між містами Одеса — Енергодар: 422 км" in text, f"need to check"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydistancenofrom ##pytest -s -m companydistancenofrom
    def test_company_distance_no_from(self, browser): #need to fix
        print("\ntest_company_distance_no_from")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_DISTANCE)
            assert "distance-calculation" in page.browser.current_url , f"link isn't equal " 

            # page.input_form(*Company.COMPANY_DISTANCE_FROM, "О")
            # page.input_form(*Company.COMPANY_DISTANCE_FROM, "д")
            # time.sleep(2)
            # page.button_click(*Company.COMPANY_DISTANCE_FROM_ODESA)
            page.input_form(*Company.COMPANY_DISTANCE_WHERE, "Е")
            page.input_form(*Company.COMPANY_DISTANCE_WHERE, "н")
            time.sleep(2)
            page.button_click(*Company.COMPANY_DISTANCE_WHERE_ENERGODAR)

            page.button_click(*Company.COMPANY_DISTANCE_AGREE_BUTTON)

            text = page.browser.find_element(*Company.COMPANY_DISTANCE_ANSWER)
            text = text.text
            print(text)
            assert "Відстань між містами Одеса — Енергодар: 422 км" in text, f"hole is OK"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companydistancenowhere ##pytest -s -m companydistancenowhere
    def test_company_distance_no_where(self, browser): #need to fix
        print("\ntest_company_distance_no_where")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_DISTANCE)
            assert "distance-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_DISTANCE_FROM, "О")
            page.input_form(*Company.COMPANY_DISTANCE_FROM, "д")
            time.sleep(2)
            page.button_click(*Company.COMPANY_DISTANCE_FROM_ODESA)
            # page.input_form(*Company.COMPANY_DISTANCE_WHERE, "Е")
            # page.button_click(*Company.COMPANY_DISTANCE_WHERE_ENERGODAR)

            page.button_click(*Company.COMPANY_DISTANCE_AGREE_BUTTON)

            text = page.browser.find_element(*Company.COMPANY_DISTANCE_ANSWER)
            text = text.text
            print(text)
            assert "Відстань між містами Одеса — Енергодар: 422 км" in text, f"hole is OK"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

############################### FUEL ##################################

    @pytest.mark.companyfuelgasoline ##pytest -s -m companyfuelgasoline
    def test_company_fuel_gasoline(self, browser): #need to fix
        print("\ntest_company_fuel_gasoline")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            time.sleep(2)
            page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Відстань між містами Рівне — Суми: 730 км" in text, f"hole is OK"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyfuelgasolinetxt ##pytest -s -m companyfuelgasolinetxt
    def test_company_fuel_gasoline_txt(self, browser): #need to fix
        print("\ntest_company_fuel_gasoline_txt")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            time.sleep(2)
            page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Паливо (бензин):" in text, f"BUG"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyfuelgas ##pytest -s -m companyfuelgas
    def test_company_fuel_gas(self, browser): #need to fix
        print("\ntest_company_fuel_gas")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            time.sleep(2)
            page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)
            page.button_click(*Company.COMPANY_FUEL_GAS)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Паливо (газ):" in text, f"BUG"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyfueldisel ##pytest -s -m companyfueldisel
    def test_company_fuel_disel(self, browser): #need to fix
        print("\ntest_company_fuel_disel")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            time.sleep(2)
            page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)
            page.button_click(*Company.COMPANY_FUEL_DISEL)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Паливо (дизель):" in text, f"BUG"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyfuelgasolinenofrom ##pytest -s -m companyfuelgasolinenofrom
    def test_company_fuel_gasoline_no_from(self, browser): #need to fix
        print("\ntest_company_fuel_gasoline_no_from")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            # page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            # page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            # time.sleep(2)
            # page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Паливо (бензин):" in text, f"hole is OK"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companyfuelgasolinenowhere ##pytest -s -m companyfuelgasolinenowhere
    def test_company_fuel_gas_no_where(self, browser): #need to fix
        print("\ntest_company_fuel_gas_no_where")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_FUEL)
            assert "fuel-calculation" in page.browser.current_url , f"link isn't equal " 

            page.input_form(*Company.COMPANY_FUEL_FROM, "Р")
            page.input_form(*Company.COMPANY_FUEL_FROM, "і")
            time.sleep(2)
            page.button_click(*Company.COMPANY_FUEL_FROM_RIVNE)
            # page.input_form(*Company.COMPANY_FUEL_WHERE, "С")
            # page.button_click(*Company.COMPANY_FUEL_WHERE_SUMI)
            
            page.button_click(*Company.COMPANY_FUEL_GAS)

            page.button_click(*Company.COMPANY_FUEL_AGREE)

            text = page.browser.find_element(*Company.COMPANY_FUEL_ANSWER)
            text = text.text
            print(text)
            assert "Паливо (газ):" in text, f"hole is OK"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


############################# STATISTIC ##############################
        
    @pytest.mark.companystatistic ##pytest -s -m companystatistic
    def test_company_statistic(self, browser): #need to fix
        print("\ntest_company_statistic")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_STATISTIC)
            assert "company/statistics" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Company.COMPANY_STATISTIC_QUARTER)
            page.button_click(*Company.COMPANY_STATISTIC_QUARTER_MONTH)
            page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "6" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_DISTANCE)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_DISTANCE)
            text = text.text
            print(text)
            assert "2142" in text, f"BUG"

            
            page.button_click(*Company.COMPANY_STATISTIC_TIME)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_TIME)
            text = text.text
            print(text)
            assert "244" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_ALL)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_ALL)
            text = text.text
            print(text)
            assert "65 910" in text, f"BUG"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companystatisticquarter ##pytest -s -m companystatisticquarter
    def test_company_statistic_quarter(self, browser): #need to fix
        print("\ntest_company_statistic_quarter")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_STATISTIC)
            assert "company/statistics" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Company.COMPANY_STATISTIC_QUARTER)
            page.button_click(*Company.COMPANY_STATISTIC_QUARTER_MONTH)
            page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "6" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_DISTANCE)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_DISTANCE)
            text = text.text
            print(text)
            assert "2142" in text, f"BUG"

            
            page.button_click(*Company.COMPANY_STATISTIC_TIME)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_TIME)
            text = text.text
            print(text)
            assert "244" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_ALL)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_ALL)
            text = text.text
            print(text)
            assert "65 910" in text, f"BUG"




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companystatisticdriver ##pytest -s -m companystatisticdriver
    def test_company_statistic_driver(self, browser): #need to fix
        print("\ntest_company_statistic_driver")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_STATISTIC)
            assert "company/statistics" in page.browser.current_url , f"link isn't equal " 

            text = page.browser.find_element(*Company.COMPANY_STATISTIC_DRIVER)
            text = text.text
            print(text)
            assert "Мягколап кисик мягколапик" in text, f"BUG"
            page.button_click(*Company.COMPANY_STATISTIC_DRIVER)

            assert "company/drivers" in page.browser.current_url , f"link isn't equal "




            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.companystatisticmonth ##pytest -s -m companystatisticmonth
    def test_company_statistic_month(self, browser): #need to fix
        print("\ntest_company_statistic_month")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_STATISTIC)
            assert "company/statistics" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Company.COMPANY_STATISTIC_MONTH)
            page.button_click(*Company.COMPANY_STATISTIC_MONTH_MONTH)
            page.button_click(*Company.COMPANY_STATISTIC_CARGO)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_CARGO)
            text = text.text
            print(text)
            assert "4" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_DISTANCE)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_DISTANCE)
            text = text.text
            print(text)
            assert "1283" in text, f"BUG"

            
            page.button_click(*Company.COMPANY_STATISTIC_TIME)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_TIME)
            text = text.text
            print(text)
            assert "244" in text, f"BUG"

            page.button_click(*Company.COMPANY_STATISTIC_ALL)
            text = page.browser.find_element(*Company.COMPANY_STATISTIC_ALL)
            text = text.text
            print(text)
            assert "41 600" in text, f"BUG"

            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

############################ BILING ##########################

    @pytest.mark.companybiling ##pytest -s -m companybiling
    def test_company_biling(self, browser): 
        print("\ntest_company_biling")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            page.button_click(*Company.COMPANY_BILING)
            assert "company/balance" in page.browser.current_url , f"link isn't equal " 

       
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ####################### OPERATOR ######################################

    @pytest.mark.companyoperator ##pytest -s -m companyoperator
    def test_company_operator(self, browser): 
        print("\ntest_company_operator")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            
            page.button_click(*Company.COMPANY_HELP)
            assert "company/help-map" in page.browser.current_url , f"link isn't equal " 

            page.button_click(*Company.COMPANY_HELP_ORDER)
            assert "company/help-order" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_HELP_CAR)
            assert "company/help-transport" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_HELP_DRIVER)
            assert "company/help-driver" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_HELP_COSTOMER)
            assert "company/help-clients" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_HELP_EMPLOYEE)
            assert "help-employees" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_HELP_MAP)
            assert "company/help-map" in page.browser.current_url , f"link isn't equal "

       
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

        ####################### MESSAGE ######################################

    @pytest.mark.companymessage ##pytest -s -m companymessage
    def test_company_message(self, browser): 
        print("\ntest_company_message")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            
            page.button_click(*Company.COMPANY_MESSAGE)
            text = page.browser.find_element(*Company.COMPANY_MESSAGE_TXT)
            text = text.text
            print(text)
            assert "Останні повідомлення" in text, f"BUG"

            page.button_click(*Company.COMPANY_MESSAGE_SETTINGS)
            assert "company/profile" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_MESSAGE_SETTINGS_BACK)
            assert "company/profile" in page.browser.current_url , f"link isn't equal "
  
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

######################## PROFILE ######################################

    @pytest.mark.companyprofile ##pytest -s -m companyprofile
    def test_company_profile(self, browser): 
        print("\ntest_company_profile")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15) 
            page.browser.set_window_size(1920, 1080)  
            page.open() 
            page.go_token()
            page.entry_to_company()

            
            page.button_click(*Company.COMPANY_PROFILE)
            page.button_click(*Company.COMPANY_PROFILE_MY_PROFILE)
            assert "company/profile" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_PROFILE)
            page.button_click(*Company.COMPANY_PROFILE_FEEDBACK)
            assert "company/feedback" in page.browser.current_url , f"link isn't equal "

            page.button_click(*Company.COMPANY_PROFILE)
            page.button_click(*Company.COMPANY_PROFILE_EXIT)
            assert "uk/driver" in page.browser.current_url , f"link isn't equal "
  
            time.sleep(5)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    #pytest -s test_company.py