



from .locators import Company, Footer, Header, Service
from selenium.webdriver.common.keys import Keys 
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import os



class MainPage(BasePage):
    

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs) #Как вы уже знаете, метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.
    def alert (self):
        alert = self.browser.switch_to.alert
        msg = alert.text()

    def button_click(self, how, what):
        try:
            all_buttons = self.browser.find_element(how, what)
            actions = ActionChains(self.browser)
            actions.move_to_element(all_buttons)
            actions.perform()
            all_buttons.click()
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def button_click_light(self, how, what):
        try:
            all_buttons = self.browser.find_element(how, what)
            all_buttons.click() 
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def input_form(self, how, what,data):
        try:
            self.data = data
            all_buttons = self.browser.find_element(how, what)
            actions = ActionChains(self.browser)
            actions.move_to_element(all_buttons)
            actions.perform()
            all_buttons.send_keys(data)
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def clear_and_write_form(self, how, what, data):
        try:
            self.data = data
            all_buttons = self.browser.find_element(how, what)
            actions = ActionChains(self.browser)
            actions.move_to_element(all_buttons)
            actions.perform()
            all_buttons.send_keys(Keys.CONTROL + "a")
            all_buttons.send_keys("\b")
            all_buttons.send_keys(data)
             ##("\b\b\b\b\b\b")
             # page.input_form(*Company.COMPANY_CUSTOMERS_EDIT_NAME, Keys.DELETE)
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def clear_form(self, how, what):
        try:
            
            all_buttons = self.browser.find_element(how, what)
            actions = ActionChains(self.browser)
            actions.move_to_element(all_buttons)
            actions.perform()
            all_buttons.send_keys(Keys.CONTROL + "a")
            all_buttons.send_keys("\b")
            
             ##("\b\b\b\b\b\b")
             # page.input_form(*Company.COMPANY_CUSTOMERS_EDIT_NAME, Keys.DELETE)
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True


    def send_file(self, how, what,data):
        try:
            self.data = data
            file_path = os.path.join(data)
            all_buttons = self.browser.find_element(how, what)
            actions = ActionChains(self.browser)
            actions.move_to_element(all_buttons)
            actions.perform()
            #all_buttons.click()
            all_buttons.send_keys(file_path)
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def drop_down(self, how, what,data):
        try:
            self.data = data
            select_buttons = Select (self.browser.find_element(how, what))
            select_buttons.select_by_visible_text(data) 
            time.sleep(2)
        except (NoSuchElementException):
            return False
        return True

    def moderetion_site(self):
        

        try:
            moderetion_login ="svetlana"
            moderetion_pass = "3NRHA4PL9p8x37Bm"
            self.input_form(*Header.MODERETION_LOGIN, moderetion_login)
            self.input_form(*Header.MODERETION_PASS, moderetion_pass)
            self.button_click_light(*Header.MODERETION_BUTTON)
            self.button_click_light(*Header.MODERETION_VERIFICATION)
            self.button_click_light(*Header.MODERETION_VERIFICATION_PHONE)
            code = self.browser.find_element(By.CSS_SELECTOR, "div.driver-activation-codes.ng-scope div.registration-codes-wrapper:nth-child(2) tbody:nth-child(1) tr.ng-scope td:nth-child(2) span.ng-scope > b.ng-binding")
            code = code.text
            return code

        except (NoSuchElementException):
            return False
        return True

    def peace_of_driver_form(self,name):
        try:
            self.input_form(*Header.HEADER_DRIVER_REGISTER_MARK_CAR, name)
            self.input_form(*Header.HEADER_DRIVER_REGISTER_YEAR_CAR, "2020")
            self.input_form(*Header.HEADER_DRIVER_REGISTER_NUMBER_CAR, name)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR) 
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_CATEGORY_CAR_TRUCK) 
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR)
            self.button_click(*Header.HEADER_DRIVER_REGISTER_TYPE_CAR_TENT)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            self.button_click(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR_UPPER)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_TYPE_DOWNLOAD_CAR)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR_CMR)
            self.button_click_light(*Header.HEADER_DRIVER_REGISTER_PERMISSION_CAR)
            self.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_LENGTH_CAR, 10) 
            self.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_HEIGHT_CAR, 10)
            self.input_form(*Header.HEADER_DRIVER_REGISTER_DIMENSIONS_WIDTH_CAR, 10)
            self.input_form(*Header.HEADER_DRIVER_REGISTER_VOLUME_CAR, 10)
            self.input_form(*Header.HEADER_DRIVER_REGISTER_CAPACITY_CAR, 10) 
            button = self.browser.find_element(*Header.HEADER_DRIVER_REGISTER_AGREE_CAR)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            time.sleep(2)

        except (NoSuchElementException):
            return False
        return True

    def execute(self, how, what):
        try:
            button = self.browser.find_element(how,what)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()

        except (NoSuchElementException):
            return False
        return True

    def agree_button (self):#################Доделать
        text_alert = self.browser.find_element(*Header.HEADER_DRIVER_ALERT_TEXT)
        text_alert = text_alert.text

        text = self.browser.find_element(*Header.HEADER_DRIVER_AGREE_TEXT)
        text = text.text

        if text > 0:
            assert "Будь ласка, коректно заповніть усі обов'язкові поля, а в разі необхідності користуйтеся підказками" in text , f"link isn't equal "
        elif text_alert > 0:
            print('something wrong')
        time.sleep(2)

    def assert_text(self,how,what):

        text = self.browser.find_element(how,what)
        text = text.text

    def buttons_for_qa(self):
        self.button_click(*Footer.BUTTON_BACK_QA)
        assert "faq" in self.browser.current_url , f"link isn't equal "
        self.button_click(*Footer.BUTTON_BACK_MAIN)
        assert "nextua.transportica.com" in self.browser.current_url , f"link isn't equal "

    def failed_to_place_order(self):
        text = self.browser.find_element(*Service.MAKE_AN_ORDER_ALERT_TRY)
        text = text.text
        assert "не вдалося розмістити замовлення" in text , f"link isn't equal "

        url_text = self.browser.current_url
        if url_text == "order":
            self.button_click(*Service.MAKE_AN_ORDER_ALERT_BUTTON)
            self.button_click_light(*Service.MAKE_AN_ORDER_DELETE_BUTTON)
            self.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON)
            self.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON_SECOND)
            print ("---BUG---")



            

    def fill_in_all_required_fields(self):
        url_text = self.browser.current_url
        if url_text == self.browser.current_url:
            self.button_click(*Service.MAKE_AN_ORDER_ALERT_BUTTON)
            self.button_click_light(*Service.MAKE_AN_ORDER_DELETE_BUTTON)
            self.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON)
            self.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON_SECOND)
            print ("---BUG---")
        else:
            text = self.browser.find_element(*Service.MAKE_AN_ORDER_EMPTY_COLUMN)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "

    def go_token (self):
        token = "app_token"
        self.input_form(*Service.TOKEN, token)
        self.button_click(*Service.TOKEN_SUBMIT)

    def entry_to_company(self):
        
        self.button_click(*Header.HEADER_ENTRY)
        self.button_click(*Header.HEADER_ENTRY_FOR_COMPANY)
        self.input_form(*Header.HEADER_ALERT_PHONE, 679887888)
        self.input_form(*Header.HEADER_ALERT_PASSWORD, 12345678)
        self.button_click(*Header.HEADER_ALERT_BUTTON)
        time.sleep(3)
        assert "company/map/" in self.browser.current_url , f"link isn't equal "

    def entry_to_customer(self):
        
        self.button_click(*Header.HEADER_ENTRY)
        self.button_click(*Header.HEADER_ENTRY_FOR_CUSTOMER)
        self.input_form(*Header.HEADER_ALERT_EMAIL, "test1@m.com")
        self.input_form(*Header.HEADER_ALERT_PASSWORD_CUSTOMER, 12345)
        self.button_click(*Header.HEADER_ALERT_BUTTON_CUSTOMER)
        time.sleep(3)
        assert "cabinet/orders" in self.browser.current_url , f"link isn't equal "

    def order_in_process (self):
        text = self.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS)
        text = text.text
        print (text)
        number = self.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS_NUMBER)
        number = int(number.text)
        print (number)
        if number != 0:
               
                text = self.browser.find_element(*Company.COMPANY_ORDERS_IN_PROCESS_ORDER)
                text = text.text
                assert "В роботі" in text , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER) 
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER_BACK)
                
        else:
            
            text = self.browser.find_element(*Company.COMPANY_NO_ORDERS)
            text = text.text
            assert "Тут знаходяться замовлення, отримані" in text , f"link isn't equal "

    def order_done (self):
        text = self.browser.find_element(*Company.COMPANY_ORDERS_DONE)
        text = text.text
        assert "Виконані:" in text , f"link isn't equal " 
        number = self.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER_NUMBER)
        number = int(number.text)
        print (number)
        if number != 0:
                self.button_click(*Company.COMPANY_ORDERS_DONE)
                text = self.browser.find_element(*Company.COMPANY_ORDERS_DONE_ORDER)
                text = text.text
                assert "Виконано" in text , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER) 
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER_BACK)
                
        else:
            
            text = self.browser.find_element(*Company.COMPANY_NO_ORDERS)
            text = text.text
            assert "Тут знаходяться замовлення, отримані" in text , f"link isn't equal "

    def order_cancel (self):
        text = self.browser.find_element(*Company.COMPANY_ORDERS_CANCELED)
        text = text.text
        assert "Скасовані" in text , f"link isn't equal " 
        number = self.browser.find_element(*Company.COMPANY_ORDERS_CANCELED_ORDER_NUMBER)
        number = int(number.text)
        print (number)
        if number != 0:###### NEED TO FIX
                self.button_click(*Company.COMPANY_ORDERS_CANCELED)
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER_BACK)
                
        else:
            self.button_click(*Company.COMPANY_ORDERS_CANCELED)
            text = self.browser.find_element(*Company.COMPANY_NO_ORDERS)
            text = text.text
            assert "Немає замовлень" in text , f"link isn't equal "

    def order_offers (self):
        text = self.browser.find_element(*Company.COMPANY_ORDERS_OFFERS)
        text = text.text
        assert "Пропозиції замовлень:" in text , f"link isn't equal " 
        number = self.browser.find_element(*Company.COMPANY_ORDERS_OFFERS_NUMBER)
        number = int(number.text)
        print (number)
        if number != 0:
                self.button_click(*Company.COMPANY_ORDERS_OFFERS)
                self.button_click(*Company.COMPANY_ORDERS_OFFERS_ORDER)
                assert "driver/company/orders/order/" in self.browser.current_url , f"link isn't equal "
                self.button_click(*Company.COMPANY_ORDER_BACK)
                
        else:
            self.button_click(*Company.COMPANY_ORDERS_OFFERS)
            text = self.browser.find_element(*Company.COMPANY_NO_ORDERS)
            text = text.text
            assert "Тут знаходяться замовлення, отримані" in text , f"link isn't equal "

            




    # def button_footer(self, how, what):
    #     try:
    #         self.browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    #         time.sleep(4)
    #         all_buttons = self.browser.find_element(how, what)
    #         actions = ActionChains(self.browser)
    #         actions.move_to_element(all_buttons)
    #         actions.perform()
    #         all_buttons.click()
    #     except (NoSuchElementException):
    #         return False
    #     return True

   



       

# def drop_down_click(self, how, what,text):
#     select = Select(self.browser.find_element(how,what))
#     select.select_by_visible_text(text)



    # def alert_form_namber(self, how, what,number):
    # try:
    #         all_phone_namber = self.browser.find_element(how, what)
    #         actions = ActionChains(self.browser)
    #         actions.move_to_element(all_phone_namber)
    #         actions.perform()
    #         all_phone_namber.send_keys(number)
    # except (NoSuchElementException):
    #     return False
    # return True


        
        



    

    