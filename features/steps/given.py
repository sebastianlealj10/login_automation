from behave import given

import json

with open("test_data/config.json") as conf:
    data = json.load(conf)


@given(u'I am a registered with the {user}')
def step_given_registered_user(context, user):
    users = data["users"]
    print(users)
    if user in users:
        context.username = users[user]['username']
        context.password = users[user]['password']
    else:
        raise Exception("user no found")
