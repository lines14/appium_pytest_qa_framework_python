from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Добро пожаловать")]', 'start screen')
        self.login_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Вход"]', 'login button')
        self.by_email_button = Button(AppiumBy.XPATH, "//button[contains(., 'По email')]", 'by email button')

    def click_login_button(self):
        self.login_button.click_button()
    
    def click_by_email_button(self):
        self.by_email_button.wait_element_is_visible()
        self.by_email_button.click_button()