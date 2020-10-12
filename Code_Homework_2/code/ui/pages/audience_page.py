from base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from some_locators import AudiencePageLocators
from main_page import MainPage


class AudiencePage(BasePage):
    locators = AudiencePageLocators()

    def create_segment(self, name):
        try:

            self.click(self.locators.MENU_CREATE_SEGMENT)
        except TimeoutException:

            self.click(self.locators.MENU_CREATE_SEGMENT_IF_SEGMENT_CREATED)
            self.click(self.locators.MENU_CREATE_SEGMENT_GAMES_AND_APPS)
        finally:
            self.click(self.locators.MENU_ELEMENT_WHO_PLAYED_AND_DONATED)
            self.click(self.locators.MENU_ELEMENT2_WHO_PLAYED_AND_DONATED)
            self.click(self.locators.MENU_ADD_SEGMENT)
            elem = self.find(self.locators.INPUT_NAME_SEGMENT)
            elem.clear()
            elem.send_keys(name)
            self.click(self.locators.MENU_CREATE_SEGMENT_AFTER_ADDED_conditions)

    def check_segment(self, name):
        self.click(self.locators.INPUT_SEARCH_ELEMENTS)
        elem = self.find(self.locators.INPUT_SEARCH_ELEMENTS)
        elem.clear()
        elem.send_keys(name)
        xpath = '//li[@title="'+name+'"]'
        RESULT_SEARCH_ELEMENTS = (By.XPATH, xpath)
        self.click(RESULT_SEARCH_ELEMENTS)

    def delete_segment(self):
        self.click(self.locators.INPUT_SEARCH_ELEMENTS)
        self.click(self.locators.INPUT_DELETE_SEGMENT)
        self.click(self.locators.INPUT_MENU_WHAT_DO)
        self.click(self.locators.INPUT_MENU_DELETED_YOUR_SEGMENT)
        elem = self.find(self.locators.INPUT_SEARCH_ELEMENTS)
        elem.clear()
