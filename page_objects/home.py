from page_objects.base import BasePage
from page_objects.locators.locators import HomeLocators


class HomePage(BasePage):

    def is_user_account(self):
        return True if self.driver.find_element(*HomeLocators.USER_ACCOUNT) else False
