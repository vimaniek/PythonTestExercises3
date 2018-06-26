from Pages.BasePage import BasePage, Selector


class RegistrationPage(BasePage):
    first_name_field = Selector("#name_3_firstname")
    last_name_field = Selector("#name_3_lastname")
    martial_status_single_radio = Selector("")
    martial_status_married_radio = Selector("")
    martial_status_divorced_radio = Selector("")
    hobby_dance_checkbox = Selector("")
    hobby_reading_checkbox = Selector("")
    hobby_cricket_checkbox = Selector("")
    country_dropdown_list = Selector("")
    date_of_birth_dropdown_list = Selector("")
    month_of_birth_dropdown_list = Selector("")
    year_of_birth_dropdown_list = Selector("")
    phone_number_field = Selector("#phone_9")
    username_field = Selector("#username")
    email_field = Selector("#email_1")
    profile_picture_choose_file_button = Selector("")
    about_yourself_field = Selector("#description")
    password_field = Selector("#password_2")
    confirm_password = Selector("#confirm_password_password_2")
    submit_button = Selector("input[name = 'pie_submit'")
