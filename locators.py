from selenium.webdriver.common.by import By


class MainActivityLocators:
    IMAGE = (By.ID, 'autyzmsoft.pl.profmarcin:id/imV')
    IMAGE_AREA = (By.ID, 'autyzmsoft.pl.profmarcin:id/lObrazek')
    WORD_BUTTONS_LIST = (By.CLASS_NAME, 'android.widget.Button')
    WORD_TO_BE_GUESSED_BY_ID = (By.ID, 'autyzmsoft.pl.profmarcin:id/tvWyraz')
    BAGAIN = (By.ID, 'autyzmsoft.pl.profmarcin:id/bAgain')
    BDALEJ = (By.ID, 'autyzmsoft.pl.profmarcin:id/bDalej')


class SettingsActivityLocators:
    BMINUS = (By.ID, 'autyzmsoft.pl.profmarcin:id/btn_Minus')
    BPLUS = (By.ID, 'autyzmsoft.pl.profmarcin:id/btn_Plus')
    POZIOM = (By.ID, 'autyzmsoft.pl.profmarcin:id/tv_Poziom')
    BINFO = (By.ID, 'autyzmsoft.pl.profmarcin:id/bInfo')


class InfoActivityLocators:
    ACTION_BAR_TITLE = (By.ID, 'android:id/action_bar_title')
    BSTART = (By.ID, 'autyzmsoft.pl.profmarcin:id/bStart')
