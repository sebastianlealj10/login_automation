from selenium.webdriver.common.by import By


class LoginLocators(object):
    EMAIL_ADDRESS = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SUBMIT = (By.ID, 'SubmitLogin')


class HomeLocators(object):
    USER_ACCOUNT = (By.CLASS_NAME, 'account')
    DRESSES = (By.CSS_SELECTOR, '.menu-content > li:nth-child(2)')
    CASUAL_DRESSES = (By.CSS_SELECTOR, '.menu-content > li:nth-child(2) > .submenu-container > li:nth-child(1)')
    CASUAL_DRESSES_BANNER = (By.CLASS_NAME, '.content_scene_cat_bg')
