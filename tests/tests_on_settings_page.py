import unittest
from time import sleep
from random import randint
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

    @unittest.skip
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

    @unittest.skip
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
        Sets the number of buttons to a random value between MIN_LEVEL and MAX_LEVEL (both included)
        Then checks if there appear the same number of buttons on MainActivity
        The proces is repeated N-times for better testing
        """
        N = 3
        for i in range(0,N):
           self.__perform_difficulty_change_checking()
           self.tearDown()
           super().setUp()
           sleep(3)
           self.__go_to_settings_page()



    def __perform_difficulty_change_checking(self):

        maxl = SettingsPageTest.MAX_LEVEL
        minl = SettingsPageTest.MIN_LEVEL

        bminus = self.sa.get_bminus_button()
        bplus = self.sa.get_bminus_button()
        curr_level = int(self.sa.get_poziom_view().text)

        # Setting randowm dificulty level:
        while True:  # ensures the generated random number is different from what we initially see on the screen
            rnd_level = randint(1, 6)
            if rnd_level != curr_level: break
        delta = curr_level - rnd_level
        if delta > 0:
            klawisz = self.sa.get_bminus_button()
        else:
            klawisz = self.sa.get_bplus_button()

        print("rnd_level = ",rnd_level)
        print(f"delta: {delta}")
        print("naciskam klawisz ze znakiem ",klawisz.text )
        for i in range(0, abs(delta)):
            klawisz.click()
            sleep(0.5)

        # Going back to MainActivity and checking the number of buttons:
        self.driver.back()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        wb_list = self.ma.get_word_buttons_list()
        wb_count = len(wb_list)
        sleep(2)
        self.assertTrue(rnd_level == wb_count, "Poziom trudnosci i liczba buttonow nie zgadzają się!")



