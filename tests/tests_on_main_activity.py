import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainActivityLocators as MAL, SettingsActivityLocators as SAL
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


class MainActivityTest(BaseTest):

    # No 1 test case in documentation
    # @unittest.skip
    def test_guessed_word_presents_on_buttons(self):
        # waiting for the buttons with words to appear:
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        wb_list = self.ma.get_word_buttons_list()
        l_words = [el.text for el in wb_list]  # getting the list of words on the buttons
        guessed_word = self.ma.get_guessed_word()
        guessed_word_on_buttons: bool = (guessed_word in l_words)

        if not guessed_word_on_buttons:
            TestUtils.screen_shot(self.driver, "No proper word on any button")

        self.assertTrue(guessed_word_on_buttons,
                        "test_guessed_word_presents_on_buttons(): No proper word on any button!")

    def _are_additional_buttons_present(self):
        """Auxiliary; checks whether buttons Dalej and @ are present on the screen"""
        add_buttons_present: bool = True
        try:
            self.ma.get_bdalej_button()
            self.ma.get_bagain_button()
        except NoSuchElementException:
            add_buttons_present = False

        return add_buttons_present

    # No 2 test case in documentation
    # @unittest.skip
    def test_behaviour_after_proper_button_clicked(self):
        """
        After clicking the button with guessed word, additional buttons should appear
        and incorrect buttons should be disabled.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        # Clicking on the right button:
        wb_list, guessed_word = self.ma.click_the_proper_button()
        # Checking whether additional buttons appeared:
        sleep(2)

        additional_buttons_present = self._are_additional_buttons_present()

        # Checking whether ALL the buttons that contain incorrect words have been disabled:
        disabled_buttons_ok: bool = True
        for b in wb_list:
            if b.text != guessed_word:
                if b.get_attribute('enabled') == 'true':
                    disabled_buttons_ok = False
                    break

        # Preparing assertion messages and taking a shot of an error (if any):
        test_name = 'test_behaviour_after_proper_button_clicked()'
        msg1 = 'Additional buttons missing'
        msg2 = 'Buttons improperly disabled'

        test_ok = additional_buttons_present and disabled_buttons_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, test_name)

        self.assertTrue(test_ok, "\n" + test_name + "\n" + msg1 + " or " + msg2 + ". See screenshot.")

    # No 3 test case in documentation
    # @unittest.skip
    def test_switching_to_settings(self):
        """
        Can switch to Settings?
        Passed if there are checkable elements in the activity we switch to.
        """
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.IMAGE_AREA))
        self.ma.long_touch_on_image()
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(SAL.POZIOM))
        list_not_empty = self.sa.settings_elements_present()
        self.assertTrue(list_not_empty, "Settings did not appear!")

    @staticmethod
    def _are_all_buttons_enabled(button_list):
        for b in button_list:
            is_b_disabled = (b.get_attribute('enabled') == 'false')
            if is_b_disabled: return False
        return True

    # No 4 test case in documentation
    # @unittest.skip
    def test_clicking_on_At_button(self):
        """
        What happens after we click on @ button.
        Passed if:
        1. the number of newly created buttons equals the number of old buttons AND
        2. the new word buttons list equals the old one (order NOT important) AND
        3. all the new buttons are enabled AND
        4. guessed word remains unchanged.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        # Clicking on the right button:
        wb_list_old, guessed_word_old = self.ma.click_the_proper_button()
        w_list_old = self.ma.get_words_list()
        print(f"w_list_old = {w_list_old}")
        # Waiting for the @ button to appear:
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.BAGAIN))
        # Clicking the @ button:
        self.ma.click_on_At_button()
        sleep(1)
        # Waiting for the buttons with words to appear:
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        wb_list_new = self.ma.get_word_buttons_list()
        w_list_new = self.ma.get_words_list()
        print(f"w_list_new = {w_list_new}")

        # Checking the continton nr 1:
        test_fail_1 = not (len(wb_list_new) == len(wb_list_old))
        # Checking the continton nr 2:
        test_fail_2 = not (sorted(w_list_new) == sorted(w_list_old))
        # Checking the continton nr 3:
        test_fail_3 = not self._are_all_buttons_enabled(wb_list_new)
        # Checking the condition nr 4:
        guessed_word_new = self.ma.get_guessed_word()
        test_fail_4 = not (guessed_word_new == guessed_word_old)

        test_fail = (test_fail_1 or test_fail_2 or test_fail_3 or test_fail_4)
        # Taking the shot if an error:
        if test_fail:
            TestUtils.screen_shot(self.driver, "improper behaviour after clicking At button")
        # determining the reason(s) of negative test:
        reason = []
        if test_fail_1: reason.append("different numbers of buttons")
        if test_fail_2: reason.append("different lists of words")
        if test_fail_3: reason.append("some buttons still disabled")
        if test_fail_4: reason.append("guessed word changed")

        self.assertFalse(test_fail, f"Improper behaviour after clicking @ button! Reason: {reason}")

    # No 5 test case in documentation
    # @unittest.skip
    def test_moving_to_next_exercise(self):
        """
        What happens after we click on the button with green arrow.
        Passed if:
        1.new word buttons appear AND
        2.buttons under the picture disappeared AND
        3.the number of the new word buttons equals the number of the old ones AND
        4.all newly created buttons are enabled.
        Note: picture may not be present; it is correct, do not test this.
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        # Getting the number of buttons with words:
        old_number = len(self.ma.get_word_buttons_list())
        # Clicking the right button:
        self.ma.click_the_proper_button()
        # Waiting for the button with green arrow to appear:
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.BDALEJ))
        # Moving to the next exercise - clicking the button with green arrow:
        self.ma.click_bdalej_button()
        # Waiting for the green arrow button to disappear and new word buttons to appear:
        sleep(0.5)
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))

        # Checking the test conditions 1,2,3,4, one by one:

        # 1.Did new word buttons appear?
        new_wb_list = self.ma.get_word_buttons_list()
        new_number = len(new_wb_list)
        test_fail_1 = not (new_number > 0)

        # 2.Checking whether the buttons under the picture disappeared,
        # if we cannot find bdalej and bagain - that's OK !!!!
        # (speeding up a bit, because in proper condition the buttons in question are not present)
        self.driver.implicitly_wait(TestUtils.WAIT_TIME / 5)
        # (end speeding up)

        test_fail_2 = self._are_additional_buttons_present()

        # restoring implicit wait time - just in case... ;)
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)

        # 3.Are the numbers of new and old buttons the same?
        test_fail_3 = not (old_number == new_number)

        # 4.Are all newly created buttons active/enabled
        test_fail_4 = not self._are_all_buttons_enabled(new_wb_list)

        test_fail = test_fail_1 or test_fail_2 or test_fail_3 or test_fail_4

        if test_fail:
            TestUtils.screen_shot(self.driver, "Error while moving to the next exercise")

        # 4.Determining the reason(s) of negative test:
        reason = []
        if test_fail_1: reason.append("new word buttons did not appear")
        if test_fail_2: reason.append("green arrow button and/or @ button still present")
        if test_fail_3: reason.append("numbers of buttons in old and new exercises differ")
        if test_fail_4: reason.append("not all new buttons enabled")

        self.assertFalse(test_fail, f"Error while moving to the next exercise! Reason: {reason} See screenshot.")

    def _check_after_bad_button_clicked(self, wb_list):
        """Auxiliary; checks whether everything's OK after we clicked the wrong word button"""
        """expected cond.: additional buttons should not appear and no word button should be disabled"""
        """Parameter: wb_list: list of buttons to check their enabled state"""
        # (speeding up a bit, because in proper conditions, additional buttons are not present)
        self.driver.implicitly_wait(TestUtils.WAIT_TIME / 5)
        # If buttons 'dalej' and '@' are present - that's bad... :
        add_buttons_present = self._are_additional_buttons_present()
        # restoring WAIT_TIME:
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        if add_buttons_present:
            return False
        else:  # checking whether improper buttons are not disabled:
            all_enabled = self._are_all_buttons_enabled(wb_list)
            return all_enabled

    # No 6 test case in documentation
    # @unittest.skip
    def test_behaviour_after_improper_button_clicked(self):
        """ How the app behaves after we clicked an improper word button(s)?
        Passed if
          1. additional buttons (buttons with @ and with green arrow) do NOT appear AND
          2. no word button is disabled
        """
        # Waiting for the buttons with words to appear
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
        # Clicking all the word buttons except the right one(s) and performing check:
        guessed_word = self.ma.get_guessed_word()
        wb_list = self.ma.get_word_buttons_list()
        test_ok = True
        for b in wb_list:
            if b.text != guessed_word:
                b.click()
                sleep(1)
                test_ok = self._check_after_bad_button_clicked(wb_list)
                if not test_ok:
                    break

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Improper behavior after clicking a wrong word button")

        self.assertTrue(test_ok, "Improper behavior after clicking a wrong word button! See screenshot.")


if __name__ == '__main__':
    unittest.main()
