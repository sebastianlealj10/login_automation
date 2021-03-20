from behave import then

from page_objects.home import HomePage


@then(u'I am in the home page')
def step_then_logged(context):
    home_page = HomePage(context.driver)
    assert home_page.is_user_account()
