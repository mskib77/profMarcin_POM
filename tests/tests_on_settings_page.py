import unittest

from ddt import ddt, data
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators import MainActivityLocators, SettingsAcctivityLocators
from tests.base_test import BaseTest
from tests.helpers.auxiliaries import Auxiliaries


@ddt
class SettingsPageTest(BaseTest):
    # difficulty levels
    MAX_LEVEL = 6
    MIN_LEVEL = 1

    def setUp(self):
        """Going to Settings Activity before each test"""
        super().setUp()
        self.__go_to_settings_page()

    def __go_to_settings_page(self):
        """ Auxiliary; brings up the settings activity """
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainActivityLocators.IMAGE_AREA))
        self.ma.long_touch_on_image()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(SettingsAcctivityLocators.POZIOM))

    def __perform_difficulty_change(self, target_level):
        """
        Auxiliary; Changes difficulty level to target_level while on Settings Activity
        """
        maxl = SettingsPageTest.MAX_LEVEL
        minl = SettingsPageTest.MIN_LEVEL

        # parameter sanitization:
        if target_level not in range(minl, maxl + 1):
            raise ValueError(f"difficulty level must be betweem {maxl} and {minl}")

        curr_level = int(self.sa.get_poziom_view().text)
        delta = curr_level - target_level

        if delta > 0:
            btn_to_click = self.sa.get_bminus_button()
        else:
            btn_to_click = self.sa.get_bplus_button()

        for i in range(0, abs(delta)):
            btn_to_click.click()
            sleep(0.5)

    # @unittest.skip
    def test_increase_level_above_upper_limit(self):
        maxl = SettingsPageTest.MAX_LEVEL
        self.__perform_difficulty_change(maxl)
        bplus = self.sa.get_bplus_button()
        bplus.click()
        sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == maxl, "Maximum difficulty level set beyond allowed limit!")

    # @unittest.skip
    def test_decrease_level_below_lower_limit(self):
        minl = SettingsPageTest.MIN_LEVEL
        self.__perform_difficulty_change(minl)
        bminus = self.sa.get_bminus_button()
        bminus.click()
        sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == minl, "Minimum difficulty level set below allowed limit!")

    # @unittest.skip
    @data(1, 3, 6)
    def test_number_of_buttons_equals_difficulty_level(self, diff_level):
        """
        Sets the number of buttons to a diff_level
        Then checks if there appear the same number of buttons on MainActivity
        """
        self.__perform_difficulty_change(diff_level)
        # Going to Main Acctivity:
        self.driver.back()
        WebDriverWait(self.driver, Auxiliaries.WAIT_TIME).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        wb_list = self.ma.get_word_buttons_list()
        wb_count = len(wb_list)
        sleep(2)
        self.assertTrue(wb_count == diff_level,
                        f"Difficulty level ({diff_level}) and the number of word buttons ({wb_count}) do not match!")

    def test_switching_to_info_activity(self):
        """
        Can switch to Info?
        Passed if there are "android:id/action_bar_title informacje o aplikacji" elements in the activity we switch to.
        """
        binfo = self.sa.get_info_button()
        binfo.click()
        try:
            WebDriverWait(self.driver, Auxiliaries.WAIT_TIME).until(EC.presence_of_element_located(SettingsAcctivityLocators.ACTION_BAR_TITLE))
        except NoSuchElementException:
            test_ok = False
        else:
            test_ok = True
        finally:
            sleep(2)

        self.assertTrue(test_ok, "Info activity did not appear!")


if __name__ == '__main__':
    unittest.main()
