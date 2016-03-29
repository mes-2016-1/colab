
@then(u'The browser URL should be "{url}"')
def step_impl(context, url):
    assert context.driver.current_url.endswith(url)