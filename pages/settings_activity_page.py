from selenium.common.exceptions import NoSuchElementException

from locators import SettingsAcctivityLocators


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

    def get_bplus_button(self):
        bplus = self.driver.find_element(*SettingsAcctivityLocators.BPLUS)
        return bplus

    def get_bminus_button(self):
        bminus = self.driver.find_element(*SettingsAcctivityLocators.BMINUS)
        return bminus

    def get_poziom_view(self):
        vpoziom = self.driver.find_element(*SettingsAcctivityLocators.POZIOM)
        return vpoziom
