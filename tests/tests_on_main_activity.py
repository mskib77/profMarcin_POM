import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainActivityLocators, SettingsAcctivityLocators
from tests.base_test import BaseTest
from tests.helpers.screens import screen_shot


class MainActivityTest(BaseTest):

    @unittest.skip
    def test_guessed_word_present_on_buttons(self):
        # waiting for buttons with words to appear
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        wb_list = self.ma.get_word_buttons_list()
        l_words = [el.text for el in wb_list]  # getting the list of words on the buttons
        guessed_word = self.ma.get_guessed_word()
        guessed_word_on_buttons: bool = (guessed_word in l_words)

        if not guessed_word_on_buttons:
            screen_shot(self, "No proper word on any button")

        self.assertTrue(guessed_word_on_buttons,
                        "test_guessed_word_presence_on_buttons(): No proper word on any button!")

    @unittest.skip
    def test_proper_behaviour_after_right_word_button_clicked(self):
        """
        After clicking the button with guessed word, additional buttons should appear
        and incorrect buttons should be disabled.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        # Clicking on the right button:
        wb_list, guessed_word =self.ma.click_the_proper_button()
        # Checking whether additional buttons appeared:
        sleep(2)
        additional_buttons_ok: bool = True
        try:
            bdalej = self.ma.get_bdalej_button()
            bagain = self.ma.get_bagain_button()
        except NoSuchElementException:
            additional_buttons_ok = False

        # Checking whether buttons that contains incorrect words have been disabled:
        disabled_buttons_ok: bool = True
        for b in wb_list:
            if b.text != guessed_word:
                if b.get_attribute('enabled') == 'true':
                    disabled_buttons_ok = False
                    break

        # Preparing assertion messages and taking a shot of an error (if any):
        test_name = 'test_proper_behaviour_after_right_word_button_clicked()'
        msg1 = 'Additional buttons missing'
        msg2 = 'Buttons improperly disabled'

        test_ok = additional_buttons_ok and disabled_buttons_ok

        if not test_ok:
            screen_shot(self, test_name)

        self.assertTrue(test_ok, "\n" + test_name + "\n" + msg1 + " or " + msg2 + ". See picture.")

    @unittest.skip
    def test_switching_to_settings(self):
        """
        Can switch to Settings?
        Passed if there are checkable elements in the activity we switch to.
        """
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainActivityLocators.IMAGE_AREA))
        self.ma.long_touch_on_image()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(SettingsAcctivityLocators.POZIOM))
        list_not_empty = self.sa.settings_elements_present()
        self.assertTrue(list_not_empty, "Settings did not appear!")

    @unittest.skip
    def test_clicking_on_At_button(self):
        """
        What happens after we click on @ button.
        Passed if:
        1. the number of new buttons equals the number of old buttons AND
        2. the new word buttons list equals the old one (order NOT important) AND
        3. all the new buttons are enabled AND
        3. guessed word remains unchanged.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        # Clicking on the right button:
        wb_list_old, guessed_word_old =self.ma.click_the_proper_button()
        w_list_old = self.ma.get_words_list()
        print(f"w_list_old = {w_list_old}")
        # Waiting for the @ button to appear:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.BAGAIN))
        # Clicking the @ button:
        self.ma.click_on_At_button()
        # Waiting for the buttons with words to appear:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        wb_list_new =self.ma.get_word_buttons_list()
        w_list_new =self.ma.get_words_list()
        print(f"w_list_new = {w_list_new}")

        # Checking the continton nr 1:
        test_fail_1 = not (len(wb_list_new) == len(wb_list_old))
        # Checking the continton nr 2:
        test_fail_2 = not (sorted(w_list_new) == sorted(w_list_old))
        # Checking the continton nr 3:
        test_fail_3 = False
        for b in wb_list_new:
            test_fail_3 = (b.get_attribute('enabled') == 'false')
            if test_fail_3: break
        # Checking the condition nr 4:
        guessed_word_new =self.ma.get_guessed_word()
        test_fail_4 = not (guessed_word_new == guessed_word_old)

        test_fail = (test_fail_1 or test_fail_2 or test_fail_3 or test_fail_4)
        # Taking the shot if an error:
        if test_fail:
            screen_shot(self, "improper behaviour after clicking At button")
        # determining reason(s) of the negative test:
        reason = []
        if test_fail_1: reason.append("different numbers of buttons")
        if test_fail_2: reason.append("different lists of words")
        if test_fail_3: reason.append("some buttons still disabled")
        if test_fail_4: reason.append("change of the guessed word")

        self.assertFalse(test_fail, f"Improper behaviour after clicking @ button! Reason: {reason}")

    def test_moving_to_next_exercise(self):
        """
        What happens after we click on the button with green arrow.
        Passed if:
        1.new word buttons appear AND
        2.buttons under the picture disappeared AND
        3.the number of the new word buttons equals the number of the old ones.
        Note: picture may not be present; it is correct, do not test this.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
        # Getting the number of buttons with words:
        old_number = len(self.ma.get_word_buttons_list())
        # Clicking the right button:
        self.ma.click_the_proper_button()
        # Waiting for the additional buttons to appear:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainActivityLocators.BDALEJ))
        # Moving to the next exercise - clicking the button with a green arrow:
        self.ma.click_bdalej_button()
        # Waiting for the new word buttons to appear:
        sleep(2)

        # Checking the test conditions 1,2,3,4, one by one:

        # 1.Did new buttons appear?
        new_number = len(self.ma.get_word_buttons_list())
        test_fail_1 = not (new_number > 0)

        # 2.Checking whether the buttons under the picture disappeared:
        try:
            self.ma.get_bdalej_button()
            test_fail_2 = True
        except NoSuchElementException:
            test_fail_2 = False

        try:
            self.ma.get_bagain_button()
            test_fail_3 = True
        except NoSuchElementException:
            test_fail_3 = False

        # 3.Are the numbers of new and old buttons the same?
        test_fail_4 = not (old_number == new_number)

        test_fail = test_fail_1 or test_fail_2 or test_fail_3 or test_fail_4

        if test_fail:
            screen_shot(self, "Error while moving to the next exercise")

        # 4.Determining the reason(s) of negative test:
        reason = []
        if test_fail_1: reason.append("new word buttons did not appear")
        if test_fail_2: reason.append("green arrow button still present")
        if test_fail_3: reason.append("@ button still present")
        if test_fail_4: reason.append("numbers of buttons in old and new exercise differ")

        self.assertFalse(test_fail, f"Error while moving to the next exercise! Reason: {reason}")






