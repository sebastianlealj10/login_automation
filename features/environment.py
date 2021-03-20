import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

with open("test_data/config.json") as conf:
    data = json.load(conf)


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(data["urls"]['base_url'])


def after_scenario(context, scenario):
    context.driver.close()
