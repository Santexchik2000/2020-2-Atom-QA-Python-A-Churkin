from base_page import BasePage
from selenium.common.exceptions import TimeoutException
from some_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_autorization(self):
        try:
            Check_element_company = self.find(self.locators.MENU_COMPANY)
            Check_element_audiotori = self.find(self.locators.MENU_AUDITORIUMS)
            Check_element_balance = self.find(self.locators.MENU_BALANCE)
            Check_element_statisticks = self.find(
                self.locators.MENU_STATISTICKS)
            Check_element_pro = self.find(self.locators.MENU_PRO)
            Check_element_profile = self.find(self.locators.MENU_PROFILE)
            Check_element_tools = self.find(self.locators.MENU_TOOLS)
            Check_element_helps = self.find(self.locators.MENU_HELPS)

            return Check_element_company.is_displayed() and Check_element_audiotori.is_displayed() and \
                Check_element_balance.is_displayed() and Check_element_statisticks.is_displayed() and Check_element_pro.is_displayed() \
                and Check_element_profile.is_displayed() and Check_element_tools.is_displayed() and Check_element_helps.is_displayed()
        except TimeoutException:
            return False

    def go_to_audience(self):
        if self.find(self.locators.MENU_AUDITORIUMS).is_displayed():
            self.click(self.locators.MENU_AUDITORIUMS)

    def go_to_company(self):
        self.click(self.locators.MENU_COMPANY)
