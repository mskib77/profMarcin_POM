from datetime import datetime
import os


def screen_shot(self, filename):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + filename + '.png'
        self.driver.get_screenshot_as_file(store_file)