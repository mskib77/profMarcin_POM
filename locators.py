from selenium.webdriver.common.by import By


class MainActivityLocators():

    IMAGE = (By.ID, 'autyzmsoft.pl.profmarcin:id/imV')
    IMAGE_AREA = (By.ID, 'autyzmsoft.pl.profmarcin:id/lObrazek')
    WORD_BUTTONS_LIST = (By.CLASS_NAME, 'android.widget.Button')
    WORD_TO_BE_GUESSED_BY_ID = (By.ID, 'autyzmsoft.pl.profmarcin:id/tvWyraz')
    WORD_TO_BE_GUESSED_BY_XPATH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    BAGAIN = (By.ID, 'autyzmsoft.pl.profmarcin:id/bAgain')
    BDALEJ = (By.ID, 'autyzmsoft.pl.profmarcin:id/bDalej')


class SettingsAcctivityLocators():

    BMINUS = (By.ID, 'autyzmsoft.pl.profmarcin:id/btn_Minus')
    BPLUS = (By.ID, 'autyzmsoft.pl.profmarcin:id/btn_Plus')
    POZIOM = (By.ID, 'autyzmsoft.pl.profmarcin:id/tv_Poziom')


