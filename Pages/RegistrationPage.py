

from Pages.BasePage import BasePage, Selector


class RegistrationPage(BasePage):
    first_name_field = Selector("#name_3_firstname")
    last_name_field = Selector("#name_3_lastname")
    martial_status_single_radio = Selector("input[value = 'single']")
    martial_status_married_radio = Selector("input[value = 'married']")
    martial_status_divorced_radio = Selector("input[value = 'divorced']")
    hobby_dance_checkbox = Selector("input[value = 'dance']")
    hobby_reading_checkbox = Selector("input[value = 'reading']")
    hobby_cricket_checkbox = Selector("input[value = 'cricket ']")
    country_dropdown_list = Selector("#dropdown_7")
    day_of_birth_dropdown_list = Selector("#dd_date_8")
    month_of_birth_dropdown_list = Selector("#mm_date_8")
    year_of_birth_dropdown_list = Selector("#yy_date_8")
    phone_number_field = Selector("#phone_9")
    username_field = Selector("#username")
    email_field = Selector("#email_1")
    profile_picture_choose_file_button = Selector("#profile_pic_10")
    about_yourself_field = Selector("#description")
    password_field = Selector("#password_2")
    confirm_password = Selector("#confirm_password_password_2")
    submit_button = Selector("input[name = 'pie_submit'")

    # sets for input fields
    def set_first_name(self, text):
        self._send_keys(self.first_name_field, text)

    def set_last_name(self, text):
        self._send_keys(self.last_name_field, text)

    def set_phone_number(self, text):
        self._send_keys(self.phone_number_field, text)

    def set_username(self, text):
        self._send_keys(self.username_field, text)

    def set_email(self, text):
        self._send_keys(self.email_field, text)

    def set_about_yourself(self, text):
        self._send_keys(self.about_yourself_field, text)

    def set_password(self, text):
        self._send_keys(self.password_field, text)

    def set_confirm_password(self, text):
        self._send_keys(self.confirm_password, text)

    # sets for hobby checkboxes
    def set_hobby_dance(self):
        self._click_element(self.hobby_dance_checkbox)

    def set_hobby_reading(self):
        self._click_element(self.hobby_reading_checkbox)

    def set_hobby_cricket(self):
        self._click_element(self.hobby_cricket_checkbox)

    # sets for martial status radio buttons
    def click_single_radio(self):
        self._click_element(self.martial_status_single_radio)

    def click_married_radio(self):
        self._click_element(self.martial_status_married_radio)

    def click_divorced_radio(self):
        self._click_element(self.martial_status_divorced_radio)

    # click buttons
    def click_submit_button(self):
        self._click_element(self.submit_button)

    # set for dropdown list
    def set_country_dropdown_list(self, value):
        self._set_dropdown_list(self.country_dropdown_list, value)

    def set_date_of_birth(self, day, month, year):
        self._set_dropdown_list(self.day_of_birth_dropdown_list, day)
        self._set_dropdown_list(self.month_of_birth_dropdown_list, month)
        self._set_dropdown_list(self.year_of_birth_dropdown_list, year)

    # set for upload picture path
    def upload_picture(self, path):
        self._send_keys(self.profile_picture_choose_file_button, path)
