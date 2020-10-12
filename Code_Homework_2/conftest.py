import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def config(request):
    selenoid = request.config.getoption('--selenoid')
    download_dir = request.config.getoption('--download_dir')
    return {'selenoid': selenoid, 'download_dir': download_dir}


def pytest_addoption(parser):
    parser.addoption('--selenoid', default=None)
    parser.addoption('--download_dir', default='/tmp')


@pytest.fixture(scope='function')
def driver(config):
    driver = None

    if config['selenoid']:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "80.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False
            }
        }
        selenoid_url = 'http://' + config['selenoid'] + '/wd/hub'
        options = ChromeOptions()
        driver = webdriver.Remote(
            command_executor=selenoid_url, options=options, desired_capabilities=capabilities)
        driver.file_detector = LocalFileDetector()
    else:

        options = ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install(
        ), options=options, desired_capabilities=DesiredCapabilities().CHROME)
    driver.maximize_window()
    driver.get('https://target.my.com/')
    yield driver
    driver.quit()
