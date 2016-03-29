from selenium import webdriver


def before_all(context):
    context.server_url = "http://localhost:8000"

def before_feature(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(500)

def after_feature(context, scenario):
    context.driver.quit()