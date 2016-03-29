

@when(u'I access the URL "{url}"')
def step_impl(context, url):
    context.driver.get(context.base_url + "/")


@when(u'I click in "{link}"')
def step_impl(context, link):
    context.driver.find_element_by_link_text(link).click()