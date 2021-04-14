from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainActivityLocators, SettingsAcctivityLocators
from tests.base_test import BaseTest


class SettingsPageTest(BaseTest):
    # difficulty levels
    MAX_LEVEL = 6
    MIN_LEVEL = 1

    def setUp(self):
        super().setUp()
        self.__go_to_settings_page()

    def __go_to_settings_page(self):
        """ Auxiliary; brings up the settings activity """
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainActivityLocators.IMAGE_AREA))
        self.ma.long_touch_on_image()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(SettingsAcctivityLocators.POZIOM))

    def test_increase_level_above_upper_limit(self):
        maxl = SettingsPageTest.MAX_LEVEL
        bplus = self.sa.get_bplus_button()
        curr_level = int(self.sa.get_poziom_view().text)
        # Trying to exceed MAX_LEVEL:
        for i in range(curr_level, maxl + 1):
            bplus.click()
            sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == maxl, "Maximum difficulty level set beyond allowed limit!")

    def test_decrease_level_below_lower_limit(self):
        minl = SettingsPageTest.MIN_LEVEL
        bminus = self.sa.get_bminus_button()
        curr_level = int(self.sa.get_poziom_view().text)
        # Trying to go below MIN_LEVEL:
        for i in range(curr_level, minl - 1, -1):
            bminus.click()
            sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == minl, "Minimum difficulty level set below allowed limit!")

    def test_number_of_buttons_equals_difficulty_level(self):
        """
        """

