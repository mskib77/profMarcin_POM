from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from locators import MainActivityLocators


class MainActivity():

    def __init__(self, sterownik):
        self.driver = sterownik

    def long_touch_on_image(self):
        """Long touching on the image when the image is present"""
        action = TouchAction(self.driver)
        image = self.driver.find_element(*MainActivityLocators.IMAGE)
        action.long_press(image).perform()

    def long_touch_on_image_area(self):
        """Long touching on the image area when the image is absent"""
        action = TouchAction(self.driver)
        image = self.driver.find_element(*MainActivityLocators.IMAGE_AREA)
        action.long_press(image).perform()

    def get_word_buttons_list(self):
        """Returns list of buttons with words"""
        try:
            l_buttons = self.driver.find_elements(*MainActivityLocators.WORD_BUTTONS_LIST)
        except NoSuchElementException:
            l_words = []
        return l_buttons

    def get_words_list(self):
        """ Returns list of words on buttons """
        l_buttons = self.get_word_buttons_list()
        w_list = [b.text for b in l_buttons]
        return w_list

    def click_the_proper_button(self):
        """
        Clicking the button with right word on it.
        Returns the list of words buttons and the guessed word.
        """
        guessed_word = self.get_guessed_word()
        wb_list = self.get_word_buttons_list()
        # Going down one by one until the correct button:
        for b in wb_list:
            if b.text == guessed_word:
                b.click()
                break
        return wb_list, guessed_word

    def click_bdalej_button(self):
        b_dalej = self.get_bdalej_button()
        b_dalej.click()

    def get_guessed_word(self):
        guessed_word = self.driver.find_element(*MainActivityLocators.WORD_TO_BE_GUESSED_BY_ID).text
        return guessed_word

    def get_guessed_word_by_xpath(self):
        guessed_word = self.driver.find_element(*MainActivityLocators.WORD_TO_BE_GUESSED_BY_XPATH).text
        return guessed_word

    def get_bagain_button(self):
        bagain = self.driver.find_element(*MainActivityLocators.BAGAIN)
        return bagain

    def get_bdalej_button(self):
        bdalej = self.driver.find_element(*MainActivityLocators.BDALEJ)
        return bdalej

    def click_on_At_button(self):
        bAgain = self.get_bagain_button()
        bAgain.click()


