from behave import when
from page_objects.login import LoginPage


@when(u'I login into the page')
def step_when_login(context):
    login_page = LoginPage(context.driver)
    login_page.fill_username(context.username)
    login_page.fill_password(context.password)
    login_page.submit_login()
