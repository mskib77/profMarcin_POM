from selenium.common.exceptions import NoSuchElementException


class SettingsActivity():

    def __init__(self, sterownik):
        self.driver = sterownik

    def __get_checkable_elements_list(self):
        try:
            list = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        except NoSuchElementException:
            list = []
        return list

    def settings_elements_present(self):
        checkable_list = self.__get_checkable_elements_list()
        return checkable_list is not []
