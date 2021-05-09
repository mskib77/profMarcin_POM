import unittest
from ddt import ddt, data
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators import MainActivityLocators as MAL, InfoActivityLocators as IAL, SettingsActivityLocators as SAL
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


@ddt
class SettingsPageTest(BaseTest):
    # difficulty levels
    MAX_LEVEL = 6
    MIN_LEVEL = 1

    def setUp(self):
        """Going to Settings Activity before each test"""
        super().setUp()
        self._go_to_settings_page(self.driver)

    def _go_to_settings_page(self, driver):
        """ Auxiliary; brings up the Settings activity. Starts from MainActivity """
        """ Called by setUp() """
        self.ma.long_touch_on_image()
        WebDriverWait(driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(SAL.POZIOM))

    def _perform_difficulty_change(self, target_level):
        """Auxiliary; Changes difficulty level to target_level while on Settings Activity"""
        maxl = SettingsPageTest.MAX_LEVEL
        minl = SettingsPageTest.MIN_LEVEL

        # parameter sanitization:
        if target_level not in range(minl, maxl + 1):
            raise ValueError(f"difficulty level must be between {maxl} and {minl}")

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
    # test No 7 in documentation
    def test_increase_level_above_upmost_limit(self):
        maxl = SettingsPageTest.MAX_LEVEL
        self._perform_difficulty_change(maxl)
        bplus = self.sa.get_bplus_button()
        bplus.click()
        sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == maxl, f"Difficulty level ({curr_level}) was set above allowed limit!")

    # @unittest.skip
    # test No 8 in documentation
    def test_decrease_level_below_lowest_limit(self):
        minl = SettingsPageTest.MIN_LEVEL
        self._perform_difficulty_change(minl)
        bminus = self.sa.get_bminus_button()
        bminus.click()
        sleep(0.5)
        curr_level = int(self.sa.get_poziom_view().text)
        self.assertTrue(curr_level == minl, f"Difficulty level ({curr_level}) was set below allowed limit!")

    # @unittest.skip
    # test No 9 in documentation
    @data(1, 2, 6)
    def test_number_of_buttons_equals_difficulty_level(self, diff_level):
        """
        Sets the number of buttons to a diff_level
        Then checks if there appear the same number of buttons on MainActivity
        """
        self._perform_difficulty_change(diff_level)
        # Going to Main Acctivity:
        self.driver.back()
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        wb_list = self.ma.get_word_buttons_list()
        wb_count = len(wb_list)
        sleep(2)
        self.assertTrue(wb_count == diff_level,
                        f"Difficulty level ({diff_level}) and the number of word buttons ({wb_count}) do not match!")

    # @unittest.skip
    # test No 10 in documentation
    def test_switching_to_info_activity(self):
        """
        Can switch to Info?
        Passed if:
        1. there is "android:id/action_bar_title element in the activity we switch to AND
        2. it contains "Informacje o aplikacji" text
        """
        binfo = self.sa.get_info_button()
        binfo.click()
        test_ok = False
        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(IAL.ACTION_BAR_TITLE))
            el = self.ia.get_action_bar_title()
            if el.text.upper() == "Informacje o aplikacji".upper():
                test_ok = True
        except TimeoutException:
            test_ok = False
        finally:
            sleep(2)

        self.assertTrue(test_ok, "Info activity did not appear!")


if __name__ == '__main__':
    unittest.main()
