import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


import datetime
import pytest
from selenium.webdriver.common.by import By

from some_fixtures import *
from base import BaseCase


class Test(BaseCase):

    # @pytest.mark.skip
    @pytest.mark.UI
    @pytest.mark.parametrize('email_password', [('anchurkin1999@gmail.com', '498466'), ('grergwergb', '48hetrhert')])
    def test_negative_authorization(self, email_password):
        self.base_page.authorization(*email_password)
        with pytest.raises(AssertionError):
            assert self.main_page.check_autorization()

    # @pytest.mark.skip
    @pytest.mark.UI
    @pytest.mark.parametrize('BUTTON_LOCATOR', ['BUTTON_AUTHORIZATION_BODY_LOCATOR', 'BUTTON_AUTHORIZATION_HEAD_LOCATOR'])
    def test_button_authorization(self, BUTTON_LOCATOR: str):
        locator = getattr(self.base_page.locators, BUTTON_LOCATOR)
        self.base_page.click(locator)
        assert "Вход в рекламный кабинет" in self.driver.page_source

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_button_registration(self):
        self.base_page.click(
            self.base_page.locators.BUTTON_AUTHORIZATION_BODY_LOCATOR)
        self.base_page.click(self.base_page.locators.BUTTON_CREATE_ACCOUNT)
        assert "Регистрация" in self.driver.page_source

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_authorization(self):
        self.base_page.authorization(
            self.base_page.email, self.base_page.password)
        assert self.main_page.check_autorization()
        assert "anchurkin1999@gmail.com" in self.driver.page_source

    

    # @pytest.mark.skip

    @pytest.mark.UI
    def test_create_segment_and_check(self, auto_autorization):
        self.main_page: MainPage = auto_autorization
        self.main_page.go_to_audience()
        name = 'Mysegments ' + datetime.datetime.today().strftime("%H:%M:%S")
        self.audience_page.create_segment(name)
        self.audience_page.check_segment(name)
        assert name in self.driver.page_source

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_delete_segment(self, auto_autorization):
        self.main_page: MainPage = auto_autorization
        self.main_page.go_to_audience()
        name = 'Mysegments ' + datetime.datetime.today().strftime("%H:%M:%S")
        self.audience_page.create_segment(name)
        self.audience_page.check_segment(name)
        self.audience_page.delete_segment()
        self.main_page.go_to_audience()
        with pytest.raises(AssertionError):
            assert name in self.driver.page_source

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_create_company_and_check(self, auto_autorization):
        self.main_page: MainPage = auto_autorization
        name = 'Mycompany ' + datetime.datetime.today().strftime("%H:%M:%S")
        self.company_page.create_company(name)
        assert self.company_page.check_company(name)
