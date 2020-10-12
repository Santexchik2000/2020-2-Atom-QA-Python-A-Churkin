import selenium
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from some_locators import BasePageLocators

RETRY_COUNT = 12
TIMEOUT = 12


class BasePage(object):
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        self.email = 'anchurkin1999@gmail.com'
        self.password = '01h014ma'
        self.path_to_file = '/home/anton/Загрузки/mockow.jpg'

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(
                    expected_conditions.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i > RETRY_COUNT - 1:
                    raise

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def authorization(self, email, password):
        self.click(self.locators.BUTTON_CREATE_MARTEKING_LOCATOR)
        self.find(self.locators.INPUT_EMAIL_AUTH_LOCATOR).send_keys(email)
        self.find(self.locators.INPUT_PASSWORD_AUTH_LOCATOR).send_keys(password)
        self.click(self.locators.BUTTON_LOG_IN_LOCATOR)
