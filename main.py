from behave.__main__ import main as behave_main

if __name__ == '__main__':
    behave_main("-f allure_behave.formatter:AllureFormatter -o allure-results features/login.feature")
