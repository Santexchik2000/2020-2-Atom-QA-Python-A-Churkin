import pytest
from audience_page import AudiencePage
from base_page import BasePage
from company_page import CompanyPage
from main_page import MainPage


@pytest.fixture
def auto_autorization(driver):
    BasePage(driver).authorization('anchurkin1999@gmail.com', '01h014ma')
    return MainPage(driver)
