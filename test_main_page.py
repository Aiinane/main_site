from dis import findlinestarts
from random import randint
import time
import pytest
from selenium import webdriver
from .pages.locators import Service
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys



email = str(randint(0,10000)) + "@m.c"
phone = int("78543" + str(randint(1000,10000))) 
name = "Auto_test"
link = "https://nextua.transportica.com/uk/"


class TestTheService():

    @pytest.mark.profitably ##pytest -m profitably
    def test_profitably(self, browser):
        print("\ntest_profitably is start")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open() 
            
            page.go_token()
            page.button_click(*Service.PROFITABLY_BUTTON)
            assert "route" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

    @pytest.mark.safely ##pytest -s -m safely
    def test_safely(self, browser):
        print("\ntest_safely is start")
        try:
            page = MainPage(browser, link)
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()

            page.button_click(*Service.SAFELY_BUTTON)
            assert "features-verified-carrier" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass

    @pytest.mark.reliably ##pytest -s -m reliably
    def test_reliably(self, browser):
        print("\ntest_reliably is start")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()

            page.button_click(*Service.RELIABLY_BUTTON)
            assert "monitoring" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

    @pytest.mark.trcoin ##pytest -s -m trcoin
    def test_trcoin(self, browser):
        print("\ntest_trcoin")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()

            page.button_click(*Service.TRCOIN_BUTTON)
            assert "tr-coin" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass
    
    @pytest.mark.businesads ##pytest -s -m businesads
    def test_busines_ads(self, browser):
        print("\ntest_busines_ads")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            time.sleep(3)
            button = page.browser.find_element(*Service.BUSINES_BUTON)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Service.BUSINES_BUTON)
            assert "naviads.com" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass

    @pytest.mark.naviads ##pytest -s -m naviads
    def test_navi_ads(self, browser):
        print("\ntest_navi_ads")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()

            page.button_click(*Service.NAVI_BUTTON)
            assert "naviads.com" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException: 
            pass

    @pytest.mark.tms ##pytest -s -m tms
    def test_tms(self, browser):
        print("\ntest_tms")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10) 
            page.browser.set_window_size(1920, 1080) 
            page.open() 
            page.go_token()
            
            time.sleep(3)
            page.button_click(*Service.TMS)
            assert "company" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass

    @pytest.mark.trmarket ##pytest -s -m trmarket
    def test_tr_market(self, browser):
        print("\ntest_tr_market")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()

            page.button_click(*Service.TR_MARKET)
            assert "nextmarket.transportica.com" in page.browser.current_url , f"link isn't equal "   

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.addad ##pytest -s -m addad
    def test_tr_add_ad(self, browser):
        print("\ntest_tr_add_ad")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()
            page.button_click(*Service.TR_MARKET_AD_ADD)
            assert "nextmarket.transportica.com" in page.browser.current_url , f"link isn't equal "   

            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 
##################################################  NOT WORK             ###############################
    # def test_tr_watch_ad(self, browser):
    #     print("\ntest_tr_watch_ad")
    #     try:
    #         page = MainPage(browser, link) 
    #         page.browser.implicitly_wait(10)  
    #         page.open() 
    #         page.go_token()
    #         time.sleep(10)
    #         button = WebDriverWait(page.browser, 10)
    #         button.until(EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[5]/div[2]/div[7]/div[2]/div[1]/div[2]/span[1]")))
    #         button.click()
    #         assert "nextmarket.transportica.com" in page.browser.current_url , f"link isn't equal "   

    #         print("\ntest is OK")
    #         page.browser.quit()
    #     except NoSuchElementException:  
    #         pass 

     ################################################################################################   

    @pytest.mark.android ##pytest -s -m android
    def test_android_button(self, browser):
        print("\ntest_android_button")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()

            page.button_click(*Service.GOOGLE_BUTTON_ONE)
            new_window = browser.window_handles[1]
            browser.switch_to.window(new_window)
            assert "play.google.com" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.app ##pytest -s -m app
    def test_app_button(self, browser):
        print("\ntest_app_button")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            time.sleep(3)

            page.button_click(*Service.APP_BUTTON_ONE)
            new_window = browser.window_handles[1]
            browser.switch_to.window(new_window)
            assert "apps.apple.com" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    @pytest.mark.apple ##pytest -s -m apple
    def test_apple_button(self, browser):##############
        print("\ntest_apple_button")
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)   
            page.open() 
            page.go_token()
            time.sleep(3)

            page.button_click(*Service.APP_BUTTON_ONE)
            new_window = browser.window_handles[1]
            browser.switch_to.window(new_window)
            assert "apps.apple.com" in page.browser.current_url , f"link isn't equal "   
            print("\ntest is OK")
            page.browser.quit()
        except NoSuchElementException:  
            pass 

    
    @pytest.mark.order ##pytest -s -m order
    def test_make_an_order(page,browser):
        print("\ntest_make_an_order")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
            page.button_click(*Service.MAKE_AN_ORDER_LEGULAR_BUTTON)
            page.button_click_light(*Service.MAKE_AN_ORDER_LEGULAR_AGREE_BUTTON)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            assert "order" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.MAKE_AN_ORDER_ALERT_BUTTON)
            page.button_click_light(*Service.MAKE_AN_ORDER_DELETE_BUTTON)
            page.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON)
            page.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON_SECOND)
            page.button_click(*Service.MAKE_AN_ORDER_BACK_BUTTON)
            assert "transportica.com" in page.browser.current_url , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.emptyorder ##pytest -s -m emptyorder
    def test_make_empty_order(page,browser):
        print("\ntest_make_empty_order")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.open() 
            page.go_token()

            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_EMPTY_COLUMN)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    
    @pytest.mark.withoutfrom ##pytest -s -m withoutfrom
    def test_make_an_order_without_from(page,browser):
        print("\ntest_make_an_order_without_from")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
 
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_ALERT_TRY)
            text = text.text
            assert "не вдалося розмістити замовлення" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutwhere ##pytest -s -m withoutwhere
    def test_make_an_order_without_where(page,browser):
        print("\ntest_make_an_order_without_where")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
    
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_ALERT_TRY)
            text = text.text
            assert "не вдалося розмістити замовлення" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutcargo ##pytest -s -m withoutcargo
    def test_make_an_order_without_cargo(page,browser):
        print("\ntest_make_an_order_without_cargo")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)

            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.button_click(*Service.MAKE_AN_ORDER_CARGO)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_EMPTY_COLUMN)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutweight ##pytest -s -m withoutweight
    def test_make_an_order_without_weight(page,browser):
        print("\ntest_make_an_order_without_weight")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_ALERT_TRY)
            text = text.text
            assert "не вдалося розмістити замовлення" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutvolume ##pytest -s -m withoutvolume
    def test_make_an_order_without_volume(page,browser):
        print("\ntest_make_an_order_without_volume")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)

            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            assert "order" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.MAKE_AN_ORDER_ALERT_BUTTON)
            page.button_click_light(*Service.MAKE_AN_ORDER_DELETE_BUTTON)
            page.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON)
            page.button_click(*Service.MAKE_AN_ORDER_DELETE_AGREE_BUTTON_SECOND)
            page.button_click(*Service.MAKE_AN_ORDER_BACK_BUTTON)
            assert "transportica.com" in page.browser.current_url , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withouttype ##pytest -s -m withouttype
    def test_make_an_order_without_type(page,browser):
        print("\ntest_make_an_order_without_type")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)

            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_EMPTY_COLUMN)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutdownload ##pytest -s -m withoutdownload
    def test_make_an_order_without_download(page,browser): #####доделать
        print("\ntest_make_an_order_without_download")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
  
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.fill_in_all_required_fields()
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutprice ##pytest -s -m withoutprice
    def test_make_an_order_without_price(page,browser): ####доделать
        print("\ntest_make_an_order_without_price")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_CUSTOMER_NAME)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.fill_in_all_required_fields()

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutname ##pytest -s -m withoutname
    def test_make_an_order_without_name(page,browser):
        print("\ntest_make_an_order_without_name")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_PHONE, phone)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_EMPTY_COLUMN)
            text = text.text
            assert "Заповніть всі обов'язкові поля" in text , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.withoutphone ##pytest -s -m withoutphone
    def test_make_an_order_without_phone(page,browser):
        print("\ntest_make_an_order_without_phone")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.MAKE_AN_ORDER_FROM, "О")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_FROM, "пр")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_FROM_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "К")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_TOWN)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "к")
            page.button_click_light(*Service.AUTOCOMPLITE_ORDER_WHERE_ADRESS)
            page.input_form(*Service.MAKE_AN_ORDER_WHERE, "1")
            page.input_form(*Service.MAKE_AN_ORDER_CARGO, name)
            page.input_form(*Service.MAKE_AN_ORDER_WEIGHT, 10)
            page.input_form(*Service.MAKE_AN_ORDER_VOLUME, 10)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_CAR)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            time.sleep(2)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD_AGREE)
            page.button_click(*Service.MAKE_AN_ORDER_TYPE_OF_DOWNLOAD)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_PRICE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.MAKE_AN_ORDER_PRICE, "15 800")
            page.input_form(*Service.MAKE_AN_ORDER_CUSTOMER_NAME, name)
            page.button_click(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            text = page.browser.find_element(*Service.MAKE_AN_ORDER_ALERT_TRY)
            text = text.text
            assert "не вдалося розмістити замовлення" in text , f"link isn't equal "

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.routecalculator ##pytest -s -m routecalculator
    def test_tarif_calculator(page,browser):
        print("\ntest_tarif_calculator")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()
    
            page.input_form(*Service.TARIFF_CALCULATOR_FROM, "О")
            page.button_click(*Service.TARIFF_CALCULATOR_FROM_AUTOCOMPLITE)
            page.input_form(*Service.TARIFF_CALCULATOR_WHERE, "К")
            page.button_click(*Service.TARIFF_CALCULATOR_WHERE_AUTOCOMPLITE)
            button = page.browser.find_element(*Service.TARIFF_CALCULATOR_TONNAGE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.TARIFF_CALCULATOR_TONNAGE, 10)
            page.button_click(*Service.TARIFF_CALCULATOR_BUTTON)
            
            assert "route" in page.browser.current_url , f"link isn't equal "
            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

####################################################### ROUTE CALCULATOR ##################

    @pytest.mark.routecalculator ##pytest -s -m routecalculator
    def test_route_calculator(page,browser):
        print("\ntest_route_calculator")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "О")
            page.button_click(*Service.ROUTE_CALCULATION_FROM_AUTOCOMPLITE)
            ##page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "К")
            button = page.browser.find_element(*Service.ROUTE_CALCULATION_WHERE_AUTOCOMPLITE)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.button_click(*Service.ROUTE_CALCULATION_WHERE_AUTOCOMPLITE)
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 10)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 1)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:##### <- need to fix
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 9)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            text = text.text
            if "Неможливо знайти такий населений пункт" in text:
                print("-----BUG----")
                page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            else:
                text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
                text = text.text
                assert "Витрати палива:" in text , f"-----BUG---- "
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)
 

            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.routecalculatorgood ##pytest -s -m routecalculatorgood
    def test_route_calculator_good(page,browser):
        print("\ntestroute_calculator_good")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 9)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 1)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 9)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # text_bool = bool(page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT))
            # print (text_bool)
            # if text_bool == True:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            # else:
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "28.71 л, вартість 29 грн." in text , f"-----BUG---- "
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.routecalculatorempty ##pytest -s -m routecalculatorempty
    def test_route_calculator_empty(page,browser):###not work
        print("\ntestroute_calculator_empty")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

          
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)
            assert "nextua.transportica" in page.browser.current_url , f"link isn't equal "


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.routecalculatorsidan ##pytest -s -m routecalculatorsidan
    def test_route_calculator_sidan(page,browser):
        print("\ntestroute_calculator_sidan")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

           
            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 9)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 1)
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 9)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
            text = text.text
            assert "Витрати палива:" in text , f"-----BUG---- "
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "28.71 л, вартість 29 грн." in text , f"-----BUG---- "
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.routecalculatordisel ##pytest -s -m routecalculatordisel
    def test_route_calculator_disel(page,browser):
        print("\ntestroute_calculator_disel")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 9)
            page.button_click(*Service.ROUTE_CALCULATION_DISEL)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            # text = text.text
            # lenght_text = len(text)
            # if lenght_text == 0:
            #     print (len(text), "need to check with hands")
            #     page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 9)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
            text = text.text
            assert "Витрати палива:" in text , f"-----BUG---- "
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "28.71 л, вартість 1 577 грн." in text , f"-----BUG---- "
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True


    @pytest.mark.routecalculatorgas ##pytest -s -m routecalculatorgas
    def test_route_calculator_gas(page,browser):
        print("\ntestroute_calculator_gas")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open()
            page.go_token() 

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 9)
            page.button_click(*Service.ROUTE_CALCULATION_GAS)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            print (text)
            text.send_keys(Keys.BACK_SPACE)
            
            #text_get = text.getText()
            #text = text.text
            #lenght_text = len(text)
            
            # # if lenght_text == 0:
            page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 1)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
            text = text.text
            assert "Витрати палива:" in text , f"-----BUG---- "
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "3.19 л, вартість 94 грн." in text , f"-----BUG---- "
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatordiselzero ##pytest -s -m calculatordiselzero
    def test_route_calculator_disel_zero(page,browser): ##need to fix
        print("\ntestroute_calculator_disel_zero")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 0)
            page.button_click(*Service.ROUTE_CALCULATION_DISEL)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 100000)

            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 0)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER_ZERO)
            text = text.text
            assert "Приблизний час у дорозі: 4 г 33 хв" in text , f"-----BUG---- "

            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatordiselone ##pytest -s -m calculatordiselone
    def test_route_calculator_disel_one(page,browser): ##need to fix
        print("\ntestroute_calculator_disel_one")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 1)
            page.button_click(*Service.ROUTE_CALCULATION_DISEL)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
  

            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            # text = text.text
            # lenght_text = len(text)
            # if lenght_text == 0:
            #     print (len(text), "need to check with hands")
            #     page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 0)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "3.19 л, вартість 175 грн." in text , f"-----BUG---- "

            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatorgaszero ##pytest -s -m calculatorgaszero
    def test_route_calculator_gas_zero(page,browser):
        print("\ntestroute_calculator_gas_zero")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open()
            page.go_token() 

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 0)
            page.button_click(*Service.ROUTE_CALCULATION_GAS)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            print (text)
            text.send_keys(Keys.BACK_SPACE)
            
            #text_get = text.getText()
            #text = text.text
            #lenght_text = len(text)
            
            # # if lenght_text == 0:
            page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 0)###asert price
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER_ZERO)
            text = text.text
            assert "Приблизний час у дорозі: 4 г 33 хв" in text , f"-----BUG---- "

            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatorgoodzero ##pytest -s -m calculatorgoodzero
    def test_route_calculator_good_zero(page,browser): #####need to fix
        print("\ntestroute_calculator_good_zero")

        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 1000000000000)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 0)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 0)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # text_bool = bool(page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT))
            # print (text_bool)
            # if text_bool == True:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            # else:
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER_ZERO)
            text = text.text
            assert "Приблизний час у дорозі: 4 г 33 хв" in text , f"-----BUG---- "
           


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatorgoodzeroprise ##pytest -s -m calculatorgoodzeroprise
    def test_route_calculator_good_zero_prise(page,browser): #####need to fix
        print("\ntestroute_calculator_good_zero_prise")

        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 1000000000000)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 0)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 10)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # text_bool = bool(page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT))
            # print (text_bool)
            # if text_bool == True:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            # else:
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER_ZERO)
            text = text.text
            assert "Приблизний час у дорозі: 4 г 33 хв" in text , f"-----BUG---- "
           


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatorgasone ##pytest -s -m calculatorgasone
    def test_route_calculator_gas_one(page,browser):
        print("\ntestroute_calculator_gas_one")
        
        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(10)  
            page.browser.set_window_size(1920, 1080)
            page.open()
            page.go_token() 

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 1)
            page.button_click(*Service.ROUTE_CALCULATION_GAS)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.button_click(*Service.ROUTE_CALCULATION_SIDAN)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
            text = text.text
            assert "Витрати палива:" in text , f"-----BUG---- "
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "3.19 л, вартість 94 грн." in text , f"-----BUG---- "
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # if "Неможливо знайти такий населений пункт" in text:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_BACK)


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True

    @pytest.mark.calculatorgoodone ##pytest -s -m calculatorgoodone
    def test_route_calculator_good_one(page,browser): #####need to fix
        print("\ntestroute_calculator_good_one")

        try:
            page = MainPage(browser, link) 
            page.browser.implicitly_wait(15)  
            page.browser.set_window_size(1920, 1080)
            page.open() 
            page.go_token()

            page.input_form(*Service.ROUTE_CALCULATION_FROM, "Запоріжжя")
            button = page.browser.find_element(*Service.MAKE_AN_ORDER_BUTTON_PUT)
            page.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            #page.browser.execute_script("window.scrollTo(0, -300);")
            page.input_form(*Service.ROUTE_CALCULATION_WHERE, "Херсон")
            page.input_form(*Service.ROUTE_CALCULATION_FUEL, 1)            
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_MAIN)
            assert "rasstoyanie" in page.browser.current_url , f"link isn't equal "
            page.input_form(*Service.ROUTE_CALCULATION_PRICE_LITR, 51.62)
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_FUEL_SECOND)
            text = text.text
            lenght_text = len(text)
            if lenght_text == 0:
                print (len(text), "need to check with hands")
                page.input_form(*Service.ROUTE_CALCULATION_FUEL_SECOND, 1)
            page.button_click(*Service.ROUTE_CALCULATION_BUTTON_EGREE)
            # text = page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT)
            # text = text.text
            # text_bool = bool(page.browser.find_element(*Service.ROUTE_CALCULATION_ALERT_TEXT))
            # print (text_bool)
            # if text_bool == True:
            #     print("-----BUG----")
            #     page.button_click(*Service.ROUTE_CALCULATION_ALERT_OK)
            # else:
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ORDER)
            text = text.text
            assert "Витрати палива:" in text , f"-----BUG---- "
            text = page.browser.find_element(*Service.ROUTE_CALCULATION_ANSWER)
            text = text.text
            assert "3.19 л, вартість 165 грн." in text , f"-----BUG---- "
           


            time.sleep(2)
            print("\ntest is OK")
            page.browser.quit()
        except (NoSuchElementException):
            return False
        return True




#pytest.main (["-s"], plugins = [TestTheService()])

#pytest -s test_main_page.py