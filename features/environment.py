import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

with open("test_data/config.json") as conf:
    data = json.load(conf)


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--remote-debugging-port=9222')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.driver.get(data["urls"]['base_url'])


def after_scenario(context, scenario):
    context.driver.close()
