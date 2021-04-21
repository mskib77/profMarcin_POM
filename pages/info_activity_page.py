from locators import InfoActivityLocators


class InfoActivity:

    def __init__(self, sterownik):
        self.driver = sterownik

    def get_action_bar_title(self):
        action_bar_tile = self.driver.find_element(*InfoActivityLocators.ACTION_BAR_TITLE)
        return action_bar_tile
