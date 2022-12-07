import time
import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.locators import Footer
from selenium.webdriver.common.keys import Keys 


link = "https://nextua.transportica.com/uk"


class TestFooter():

    def test_carrier(self, browser):
        print("\ntest_carrier")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.CARRIER_BUTTON)
            assert "driver" in page.browser.current_url , f"link isn't equal "   #id=com.poemsolutions.dispetcherdriver
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_company(self, browser):
        print("\ntest_company")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.COMPANY_BUTTON)
            assert "company" in page.browser.current_url , f"link isn't equal "   #id=com.poemsolutions.dispetcherdriver
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_tarif(self, browser):
        print("\ntest_tarif")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open()
            page.go_token() 
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.TARIFF_BUTTON)
            assert "route" in page.browser.current_url , f"link isn't equal "   #id=com.poemsolutions.dispetcherdriver
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 
        
    def test_distance(self, browser):
        print("\ntest_distance")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.DISTANCE_BUTTON)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "   #id=com.poemsolutions.dispetcherdriver
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_coin(self, browser):
        print("\ntest_coin")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.COIN_BUTTON)
            assert "tr-coin" in page.browser.current_url , f"link isn't equal "   #id=com.poemsolutions.dispetcherdriver
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_about(self, browser):
        print("\ntest_about")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.ABOUT_BUTTON)
            assert "about-us" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    def test_price_customer(self, browser):
        print("\ntest_price_customer")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.PRICE_BUTTON)
            assert "prices" in page.browser.current_url , f"link isn't equal " 
            page.button_click(*Footer.PRICE_BUTTON_CUSTOMER)
            assert "step1" in page.browser.current_url , f"link isn't equal "  
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    def test_price_shippers(self, browser):
        print("\ntest_price_shippers")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.PRICE_BUTTON)
            assert "prices" in page.browser.current_url , f"link isn't equal "   
            page.button_click(*Footer.PRICE_BUTTON_SHIPPERS)
            assert "register/driver" in page.browser.current_url , f"link isn't equal " 
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    def test_question(self, browser):
        print("\ntest_question")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.QUESTION_BUTTON)
            assert "faq" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_submit_application(self, browser):
        print("\ntest_submit_application")
        try:
            link = "https://nextua.transportica.com/uk/"
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            page.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
            page.button_click(*Footer.SUBMIT_APPLICATION)
            assert "step1" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    #################################          Q&A          ###################################

    def test_how_it_work(self, browser):
        print("\ntest_how_it_work")
        try:
            link = "https://nextua.transportica.com/uk/faq/"

            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_IT_WORK)
            assert "d-how-it-works" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    def test_change_pass(self, browser):
        print("\ntest_change_pass")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.CHANGE_PASS)
            assert "d-change-password" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_apliccation(self, browser):
        print("\ntest_application")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.APPLICATION)
            assert "d-accept-order" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass 

    def test_I_have_a_driver(self, browser):
        print("\ntest_I_have_a_driver")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.I_HAVE_A_DRIVER)
            assert "d-company-person" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_owner_of_a_car_fleet(self, browser):
        print("\ntest_owner_of_a_car_fleet")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.OWNER_OF_A_AUTOPARK)
            assert "d-autopark" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_sort_orders(self, browser):
        print("\ntest_how_to_sort_orders")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_SORT_ORDERS)
            assert "d-use-filter" in page.browser.current_url , f"link isn't equal "   
            page.buttons_for_qa()
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_money_for_delivery(self, browser):
        print("\ntest_for_delivery")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.MONEY_FOR_DELIVERY)
            assert "d-money-for-delivery" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_payment_moment(self, browser):
        print("\ntest_payment_moment")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.PAYMENT_MOMENT)
            assert "d-payment-moment" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_wrong_point(self, browser):
        print("\ntest_wrong_point")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.WRONG_POINT)
            assert "d-what-to-do" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_add_car(self, browser):
        print("\ntest_how_to_download_documents")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_ADD_CAR)
            assert "d-how-add-transport" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_take_order(self, browser):
        print("\ntest_how_to_take_order")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_TAKE_ORDER)
            assert "d-how-take-order" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_download_app(self, browser):
        print("\ntest_how_to_download_app")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_DOWNLOAD_APP)
            assert "d-where-download-apps" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_take_money(self, browser):
        print("\ntest_how_to_take_money")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_TAKE_MONEY)
            assert "d-how-take-money-for-work" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_making_price(self, browser):
        print("\ntest_how_making_price")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_MAKING_PRICE)
            assert "d-how-making-order-price" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_cancel_order(self, browser):
        print("\ntest_how_to_cancel_order")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_CANSEL_ORDER)
            assert "d-how-cancel-order" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_to_call_operator(self, browser):
        print("\ntest_how_to_call_operator")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_TO_CALL_OPERATOR)
            assert "d-how-call-operator" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_it_work_customer(self, browser):
        print("\ntest_how_it_work_customer")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_IT_WORK_CUSTOMER)
            assert "c-how-it-works" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_how_service_payment_customer(self, browser):
        print("\ntest_how_service_payment_customer")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.HOW_SERVICE_PAYMENT_CUSTOMER)
            assert "c-service-payment" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_cargo_information_customer(self, browser):
        print("\ntest_cargo_information_customer")
        try:
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.CARGO_INFORMATION_CUSTOMER)
            assert "c-cargo-information" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

    def test_where_transports_customer(self, browser):
        print("\ntest_where_transports_customer")
        try:
            link = "https://nextua.transportica.com/uk/faq/"
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10) 
            page.open()
            page.go_token()

            time.sleep(2)  
            page.button_click(*Footer.CARGO_WHERE_TRANSPORT_CUSTOMER)
            assert "c-where-transport" in page.browser.current_url , f"link isn't equal " 
            page.buttons_for_qa()  
            
            
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass 

#pytest -s test_footer.py