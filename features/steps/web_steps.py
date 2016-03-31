@when(u'I access the URL "{url}"')
def step_impl(context, url):
    context.driver.get(context.base_url + "/")


@when(u'I click in "{link}"')
def step_impl(context, link):
    context.driver.find_element_by_link_text(link).click()


@when(u'I click in "{button_value}" button')
def step_impl(context, button_value):
    context.driver.find_element_by_xpath("//input[@value='%s']|//button[.='%s']" %
                                         (button_value, button_value)).click()


@when(u'I fill "{text}" in "{field_id}" field')
def step_impl(context, text, field_id):
    field = context.driver.find_element_by_id(field_id)
    field.clear()
    field.send_keys(text)


@then(u'The field "{field_id}" should have an error')
def step_impl(context, field_id):
    field = context.driver.find_element_by_id(field_id)
    container = field.find_element_by_xpath('..')
    classes = container.get_attribute('class')
    assert 'has-error' in classes


@then(u'I should see "{content}" in "{element_id}"')
def step_impl(context, content, element_id):
    element = context.driver.find_element_by_id(element_id)
    assert content in element.text


@then(u'The browser URL should be "{url}"')
def step_impl(context, url):
    assert context.driver.current_url.endswith(url)
