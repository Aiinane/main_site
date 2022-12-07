from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class BasePage():
    #Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект.
    #  Конструктор объявляется ключевым словом __init__. 
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается примерно так
    def __init__(self, browser, url): #,timeout=5 - убрано для проверки алерта
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)  - убрано для проверки алерта

    def open(self):
        self.browser.get(self.url)

    # def go_to_login_page(self):
    #     link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
    #     link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #Чтобы перехватывать исключение, нужна конструкция try/except: 

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

#Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем: 

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

            return True

    #В классе BasePage реализуйте соответствующий метод для перехода в корзину.
    

    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                 " probably unauthorised user"