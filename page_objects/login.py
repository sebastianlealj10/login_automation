from page_objects.base import BasePage
from page_objects.locators.locators import LoginLocators


class LoginPage(BasePage):

    def fill_username(self, username):
        username_text_box = self.driver.find_element(*LoginLocators.EMAIL_ADDRESS)
        username_text_box.send_keys(username)

    def fill_password(self, password):
        password_text_box = self.driver.find_element(*LoginLocators.PASSWORD)
        password_text_box.send_keys(password)

    def submit_login(self):
        password_text_box = self.driver.find_element(*LoginLocators.SUBMIT)
        password_text_box.click()
