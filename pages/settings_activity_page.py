from selenium.common.exceptions import NoSuchElementException
from locators import SettingsAcctivityLocators
from tests.helpers.auxiliaries import WAIT_TIME


class SettingsActivity:

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

    def __scroll_to_info_button(self):
        """Auxiliary: scrolling down till the INFO button appears"""

        size: dict = self.driver.get_window_size()
        startx = size['width'] / 2;
        starty = (int)(size['height'] * 0.9);
        # endx = size['width'] / 2;
        endy = (int)(size['height'] * 0.2);

        # speeding up a little:
        self.driver.implicitly_wait(2)

        found = False
        while not found:
            try:
                self.driver.find_element(*SettingsAcctivityLocators.BINFO)
                found = True
            except NoSuchElementException:
                self.driver.swipe(startx, starty, startx, endy, 1000);

        # restoring timeout:
        self.driver.implicitly_wait(WAIT_TIME)

    def get_info_button(self):
        self.__scroll_to_info_button()
        binfo = self.driver.find_element(*SettingsAcctivityLocators.BINFO)
        return binfo
