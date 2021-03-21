from behave import given

import json

from page_objects.login import LoginPage

with open("test_data/config.json") as conf:
    data = json.load(conf)


@given(u'I am a registered with the {user}')
def step_given_registered_user(context, user):
    users = data["users"]
    if user in users:
        context.username = users[user]['username']
        context.password = users[user]['password']
    else:
        raise Exception("user no found")


@given(u'I am logged into the page as "{user}"')
def step_given_registered_user(context, user):
    users = data["users"]
    if user in users:
        context.username = users[user]['username']
        context.password = users[user]['password']
    else:
        raise Exception("user no found")

    login_page = LoginPage(context.driver)
    login_page.fill_username(context.username)
    login_page.fill_password(context.password)
    login_page.submit_login()
