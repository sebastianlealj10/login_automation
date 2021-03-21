import time

from selenium.webdriver import ActionChains

from page_objects.base import BasePage
from page_objects.locators.locators import HomeLocators


class HomePage(BasePage):

    def select_dresses(self):
        element = self.driver.find_element(*HomeLocators.DRESSES)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def select_casual_dresses(self):
        element = self.driver.find_element(*HomeLocators.CASUAL_DRESSES)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def is_user_account(self):
        return True if self.driver.find_element(*HomeLocators.USER_ACCOUNT) else False

    def is_casual_dresses_banner(self):
        return True if self.driver.find_element(*HomeLocators.USER_ACCOUNT) else False
