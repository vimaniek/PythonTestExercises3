from behave import given, when, then


@given(u'Go to a registration form by clicking on registration button on the home page.')
def step_impl(context):
    context.home.open_demo_qa()
    context.menu.click_registration_button()


@given(u'Fill fields with 0 set of data')
def step_impl(context):
    context.first_name = context.table[0][0]
    context.last_name = context.table[0][1]
    context.phone_number = context.table[0][2]
    context.username = context.table[0][3]
    context.email = context.table[0][4]
    context.about_yourself = context.table[0][5]
    context.password = context.table[0][6]
    context.confirm_password = context.table[0][7]


@given(u'Fill fields with 1 set of data')
def step_impl(context):
    context.first_name = context.table[1][0]
    context.last_name = context.table[1][1]
    context.phone_number = context.table[1][2]
    context.username = context.table[1][3]
    context.email = context.table[1][4]
    context.about_yourself = context.table[1][5]
    context.password = context.table[1][6]
    context.confirm_password = context.table[1][7]


@when(u'Fill "first_name" field with given data')
def step_impl(context):
    context.registration.set_first_name(context.first_name)


@when(u'Fill "last_name" field with given data')
def step_impl(context):
    context.registration.set_last_name(context.last_name)


@when(u'Select martial status')
def step_impl(context):
    context.registration.click_single_radio()


@when(u'Select chosen hobbies')
def step_impl(context):
    context.registration.set_hobby_dance()
    context.registration.set_hobby_reading()
    context.registration.set_hobby_cricket()


@when(u'Select country')
def step_impl(context):
    context.registration.set_country_dropdown_list("Poland")


@when(u'Select date of birth')
def step_impl(context):
    context.registration.set_date_of_birth(22, 10, 14)


@when(u'Fill "phone_number" field with given data')
def step_impl(context):
    context.registration.set_phone_number(context.phone_number)


@when(u'Fill "username" field with given data')
def step_impl(context):
    context.registration.set_username(context.username)


@when(u'Fill "email" field with given data')
def step_impl(context):
    context.registration.set_email(context.email)


@when(u'Upload profile picture')
def step_impl(context):
    context.registration.upload_picture("C:/Users/Mariusz/Downloads/download.jpg")


@when(u'Fill "about_yourself" field with given data')
def step_impl(context):
    context.registration.set_about_yourself(context.about_yourself)


@when(u'Fill "password" field with given data')
def step_impl(context):
    context.registration.set_password(context.password)


@when(u'Fill "confirm_password" field with given data')
def step_impl(context):
    context.registration.set_confirm_password(context.confirm_password)


@when(u'Click the "Submit" button')
def step_impl(context):
    context.registration.click_submit_button()


@then(u'"annotation" will appear')
def step_impl(context):
    pass
