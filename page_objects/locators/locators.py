from selenium.webdriver.common.by import By


class LoginLocators(object):
    EMAIL_ADDRESS = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SUBMIT = (By.ID, 'SubmitLogin')


class HomeLocators(object):
    USER_ACCOUNT = (By.CLASS_NAME, 'account')
