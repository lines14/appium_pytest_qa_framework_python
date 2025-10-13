from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button

class LoginScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//android.widget.TextView[@text="Забыли пароль?"]', 'login screen')
        self.forgot_password_button = Button(AppiumBy.XPATH, '//android.widget.TextView[@text="Забыли пароль?"]', 'forgot password button')
    
    def click_forgot_password_button(self):
        self.forgot_password_button.click_button()