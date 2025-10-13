from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button

class ForgotPasswordScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//button[contains(., "Выслать код")]', 'forgot password screen')
        self.send_code_button = Button(AppiumBy.XPATH, '//button[contains(., "Выслать код")]', 'send code button')

    def send_code_button_is_enabled(self):
        self.send_code_button.check_element_is_enabled()