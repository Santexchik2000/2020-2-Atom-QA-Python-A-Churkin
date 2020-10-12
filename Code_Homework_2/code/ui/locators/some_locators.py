from selenium.webdriver.common.by import By

class BasePageLocators(object):
    BUTTON_CREATE_MARTEKING_LOCATOR=(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]')
    BUTTON_AUTHORIZATION_HEAD_LOCATOR=(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')
    BUTTON_AUTHORIZATION_BODY_LOCATOR=(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]')
    BUTTON_LOG_IN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')
    DIV_INVALID_LOG_IN_LOCATOR = (By.XPATH, '//*[@id="login_form"]/div[1]/div/div[2]')
    DIV_ERROR_LOG_IN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div')
    INPUT_EMAIL_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    INPUT_PASSWORD_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    BUTTON_CREATE_ACCOUNT=(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/a')


class MainPageLocators(object):
    MENU_COMPANY=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[1]/a')
    MENU_AUDITORIUMS=(By.XPATH,'//a[@href="/segments"]')
    MENU_BALANCE=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[3]/a')
    MENU_STATISTICKS=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[4]/a')
    MENU_PRO=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[5]/a')
    MENU_PROFILE=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[6]/a')
    MENU_TOOLS=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[7]/a')
    MENU_HELPS=(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[8]/a')


class AudiencePageLocators(object):
    MENU_CREATE_SEGMENT=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div/ul/li[2]/a')
    MENU_ELEMENT_WHO_PLAYED_AND_DONATED=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/span')
    MENU_ELEMENT2_WHO_PLAYED_AND_DONATED=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/label/span')
    MENU_ADD_SEGMENT=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button/div')
    INPUT_NAME_SEGMENT=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/input')
    MENU_CREATE_SEGMENT_AFTER_ADDED_conditions=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/button/div')
    MENU_CREATE_SEGMENT_IF_SEGMENT_CREATED=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[1]/button/div')
    MENU_CREATE_SEGMENT_GAMES_AND_APPS=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[8]')

    INPUT_SEARCH_ELEMENTS=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[3]/div/div[2]/div/input')
    INPUT_DELETE_SEGMENT=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div/input')
    INPUT_MENU_WHAT_DO=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[2]/div/div/div[2]')
    INPUT_MENU_DELETED_YOUR_SEGMENT=(By.XPATH,'/html/body/div[6]/div/div/div/div/ul/li')
    

class CompanyPageLocators(object):
    MENU_CREATE_COMPANY_IF_WE_HAVENT=(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/ul/li[1]/a')
    MENU_CREATE_TRAFIK=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]')
    INPUT_LINK_FOR_CREATE=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')
    MENU_CHANGE_NAME_COMPANY=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[9]/div/div[2]/div/div[2]/input')
    BUTTON_BANNER_CLICK=(By.XPATH,'//*[@id="patterns_4"]/span')
    INPUT_PICTURE_FOR_BANNER=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/input')
    INPUT_PICTURE_DOWNOAL=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')
    INPUT_CREARE_FINAL=(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')
    INPUT_SAVE_CHANGES_AFTER_ADD_PICTURE=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[3]/div[1]/div')
    MENU_CREATE_COMPANY_AFTER_CREATE=(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div')
    MENU_DELETE_STANDART_NAME=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[9]/div/div[2]/div/div[1]')
    INPUT_FINAL2_CREATE=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button')
    MENU_SEARCH_COMPANY=(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div/input')
    