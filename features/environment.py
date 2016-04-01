from selenium import webdriver


def before_feature(context, feature):
    if 'selenium' in feature.tags:
        context.driver = webdriver.Firefox()
        context.driver.implicitly_wait(5000)
    else:
        context.driver = webdriver.PhantomJS()


def after_feature(context, feature):
    context.driver.quit()
