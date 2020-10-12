from audience_page import AudiencePage
from company_page import CompanyPage
import pytest
from _pytest.fixtures import FixtureRequest
from base_page import BasePage
from main_page import MainPage
import selenium


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.audience_page = AudiencePage(driver)
        self.company_page = CompanyPage(driver)


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.audience_page = AudiencePage(driver)
        self.company_page = CompanyPage(driver)
