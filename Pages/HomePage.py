from Pages.BasePage import BasePage, Selector


class HomePage(BasePage):
    picture_below_unique_and_clean = Selector("#post-9 > div > div:nth-child(1) > div > p:nth-child(1) > a > img")
    picture_below_customer_support = Selector("#post-9 > div > div:nth-child(2) > div > p:nth-child(1) > i > a > img")
    picture_below_very_flexible = Selector("#post-9 > div > div:nth-child(3) > div > i > a > img")
    tab1_button = Selector("a#ui-id-1")
    content1_title = Selector("#tabs-1 > b")
    tab2_button = Selector("a#ui-id-2")
    content2_title = Selector("#tabs-2 > b")
    tab3_button = Selector("a#ui-id-3")
    content3_title = Selector("#tabs-3 > b")
    tab4_button = Selector("a#ui-id-4")
    content4_title = Selector("#tabs-4 > b")
    tab5_button = Selector("a#ui-id-5")
    content5_title = Selector("#tabs-5 > b")

    def open_demo_qa(self):
        self._get_page("http://demoqa.com/")

    def click_picture_below_unique_and_clean(self):
        self._click_element(self.picture_below_unique_and_clean)

    def click_picture_below_customer_support(self):
        self._click_element(self.picture_below_customer_support)

    def click_picture_below_very_flexible(self):
        self._click_element(self.picture_below_very_flexible)

    def click_tab1_button(self):
        self._click_element(self.tab1_button)

    def click_tab2_button(self):
        self._click_element(self.tab2_button)

    def click_tab3_button(self):
        self._click_element(self.tab3_button)

    def click_tab4_button(self):
        self._click_element(self.tab4_button)

    def click_tab5_button(self):
        self._click_element(self.tab5_button)
