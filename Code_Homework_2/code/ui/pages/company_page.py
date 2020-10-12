from attr import s
from base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from some_locators import CompanyPageLocators
from main_page import MainPage
import time


class CompanyPage(BasePage):
    locators = CompanyPageLocators()

    def create_company(self, name):
        try:
            self.click(self.locators.MENU_CREATE_COMPANY_IF_WE_HAVENT)
        except TimeoutException:
            self.click(self.locators.MENU_CREATE_COMPANY_AFTER_CREATE)
        finally:
            self.click(self.locators.MENU_CREATE_TRAFIK)
            elem = self.find(self.locators.INPUT_LINK_FOR_CREATE)
            elem.send_keys("yandex.ru")
            self.click(self.locators.MENU_DELETE_STANDART_NAME)
            elem2 = self.find(self.locators.MENU_CHANGE_NAME_COMPANY)
            elem2.send_keys(name)
            self.click(self.locators.BUTTON_BANNER_CLICK)
            time.sleep(3)
            elem3 = self.find(self.locators.INPUT_PICTURE_FOR_BANNER)
            time.sleep(3)
            elem3.send_keys('/home/anton/Загрузки/mockow.jpg')
            self.click(self.locators.INPUT_PICTURE_DOWNOAL)
            self.click(self.locators.INPUT_SAVE_CHANGES_AFTER_ADD_PICTURE)
            time.sleep(3)
            self.click(self.locators.INPUT_FINAL2_CREATE)

    def check_company(self, name):
        elem = self.find(self.locators.MENU_SEARCH_COMPANY)
        elem.send_keys(name)
        XPath = '//span[text()="'+name+'"]'
        RESULT_SEARCH_COMPANY = (By.XPATH, XPath)
        try:
            self.click(RESULT_SEARCH_COMPANY)
            Xpath2 = '//div/span[text()="1"]'
            RESULT2_SEARCH_COMPANY = (By.XPATH, Xpath2)
            return self.find(RESULT2_SEARCH_COMPANY).is_displayed()
        except TimeoutException:
            return False
