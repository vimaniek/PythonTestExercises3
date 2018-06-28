from Pages.BasePage import BasePage, Selector


class MenuPage(BasePage):
    registration_button = Selector("#menu-item-374 > a")
    draggable_button = Selector("#menu-item-140 > a")
    droppable_button = Selector("#menu-item-141 > a")
    resizable_button = Selector("#menu-item-143 > a")
    selectable_button = Selector("#menu-item-142 > a")
    sortable_button = Selector("#menu-item-151 > a")
    accordion_button = Selector("#menu-item-144 > a")
    autocomplete_button = Selector("#menu-item-145 > a")
    datepicker_button = Selector("#menu-item-146 > a")
    menu_button = Selector("#menu-item-147 > a")
    slider_button = Selector("#menu-item-97 > a")
    tabs_button = Selector("#menu-item-98 > a")
    tooltip_button = Selector("#menu-item-99 > a")
    frames_and_windows_button = Selector("#menu-item-148 > a")

    def click_registration_button(self):
        self._click_element(self.registration_button)

    def click_draggable_button(self):
        self._click_element(self.draggable_button)

    def click_droppable_button(self):
        self._click_element(self.droppable_button)

    def click_resizable_button(self):
        self._click_element(self.resizable_button)

    def click_selectable_button(self):
        self._click_element(self.selectable_button)

    def click_sortable_button(self):
        self._click_element(self.sortable_button)

    def click_accordion_button(self):
        self._click_element(self.accordion_button)

    def click_autocomplete_button(self):
        self._click_element(self.autocomplete_button)

    def click_datepicker_button(self):
        self._click_element(self.datepicker_button)

    def click_menu_button(self):
        self._click_element(self.menu_button)

    def click_slider_button(self):
        self._click_element(self.slider_button)

    def click_tabs_button(self):
        self._click_element(self.tabs_button)

    def click_tooltip_button(self):
        self._click_element(self.tooltip_button)

    def click_frames_and_windows_button(self):
        self._click_element(self.frames_and_windows_button)
