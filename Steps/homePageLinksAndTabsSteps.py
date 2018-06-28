from behave import given, when, then


@given(u'I am on a http://demoqa.com/ page')
def step_impl(context):
    context.home.open_demo_qa()


@when(u'I click on a picture below "Unique & Clean" label')
def step_impl(context):
    context.home.click_picture_below_unique_and_clean()


@then(u'I will be redirect to http://demoqa.com/wp-content/uploads/2014/08/pattern-14.png page')
def step_impl(context):
    pass


@when(u'I click on a picture below "Customer Support" label')
def step_impl(context):
    context.home.open_demo_qa()
    context.home.click_picture_below_customer_support()


@when(u'I click on a picture below "Very Flexible" label')
def step_impl(context):
    context.home.open_demo_qa()
    context.home.click_picture_below_very_flexible()


@when(u'I click on the "Tab 1" button')
def step_impl(context):
    context.home.open_demo_qa()
    context.home.click_tab1_button()


@then(u'A sub-page opens with the title "Content 1 Title"')
def step_impl(context):
    pass


@when(u'I click on the "Tab 2" button')
def step_impl(context):
    context.home.click_tab2_button()


@then(u'A sub-page opens with the title "Content 2 Title"')
def step_impl(context):
    pass


@when(u'I click on the "Tab 3" button')
def step_impl(context):
    context.home.click_tab3_button()


@then(u'A sub-page opens with the title "Content 3 Title"')
def step_impl(context):
    pass


@when(u'I click on the "Tab 4" button')
def step_impl(context):
    context.home.click_tab4_button()


@then(u'A sub-page opens with the title "Content 4 Title"')
def step_impl(context):
    pass


@when(u'I click on the "Tab 5" button')
def step_impl(context):
    context.home.click_tab5_button()


@then(u'A sub-page opens with the title "Content 5 Title"')
def step_impl(context):
    pass
