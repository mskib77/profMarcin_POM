from selenium.common.exceptions import NoSuchElementException
from locators import SettingsActivityLocators
from tests.test_utils import TestUtils


class SettingsActivity:

    def __init__(self, sterownik):
        self.driver = sterownik

    def _get_checkable_elements_list(self):
        try:
            list = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        except NoSuchElementException:
            list = []
        return list

    def settings_elements_present(self):
        checkable_list = self._get_checkable_elements_list()
        return checkable_list is not []

    def get_bplus_button(self):
        bplus = self.driver.find_element(*SettingsActivityLocators.BPLUS)
        return bplus

    def get_bminus_button(self):
        bminus = self.driver.find_element(*SettingsActivityLocators.BMINUS)
        return bminus

    def get_poziom_view(self):
        vpoziom = self.driver.find_element(*SettingsActivityLocators.POZIOM)
        return vpoziom

    def _scroll_to_info_button(self):
        """Auxiliary: scrolling down till the INFO button appears"""

        x, y = TestUtils.get_screen_dimensions(self.driver)
        # speeding up a little:
        self.driver.implicitly_wait(1)
        # scrolling down till the INFO button appears:
        found = False
        while not found:
            try:
                self.driver.find_element(*SettingsActivityLocators.BINFO)
                found = True
            except NoSuchElementException:
                self.driver.swipe(x/2, y*0.9, x/2, y*0.1, 1000)
        # restoring timeout:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)

    def get_info_button(self):
        self._scroll_to_info_button()
        binfo = self.driver.find_element(*SettingsActivityLocators.BINFO)
        return binfo
