from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button

class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//android.widget.Button[@text="Вход"]', 'start screen')
        self.allow_notifications_button = Button(AppiumBy.XPATH, '//*[@text="Allow"]', 'allow notifications button')
        self.login_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Вход"]', 'login button')
        self.by_email_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="По email"]', 'by email button')

    def wait_allow_notifications_button_visible(self):
        self.allow_notifications_button.wait_element_is_visible()
    
    def click_allow_notifications_button(self):
        self.allow_notifications_button.click_button()
    
    def click_login_button(self):
        self.login_button.click_button()

    def wait_by_email_button_visible(self):
        self.by_email_button.wait_element_is_visible()
    
    def click_by_email_button(self):
        self.by_email_button.click_button()