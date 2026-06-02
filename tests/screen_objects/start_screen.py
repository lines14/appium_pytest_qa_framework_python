from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button
from main.elements.base_elements.text_box import TextBox
from config import Config


class StartScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//*[contains(@text, "Добро пожаловать")]', 'start screen') # compatible with older api-levels
        self.signIn_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Вход"]', 'login button')
        self.by_email_button = Button(AppiumBy.XPATH, "//button[contains(., 'По email')]", 'by email button')
        self.email_input_field = TextBox(AppiumBy.XPATH, "//android.view.View[@resource-id='main-layout']/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText", "email input field")
        self.password_input_field = TextBox(AppiumBy.XPATH, "//android.view.View[@resource-id='main-layout']/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText", "password input field")
        self.login_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Войти"]', 'login button')

    def click_sign_in_button(self):
        self.signIn_button.click_button()
    
    def click_by_email_button(self):
        self.by_email_button.wait_element_is_visible()
        self.by_email_button.click_button()

    def input_email(self):
        self.email_input_field.wait_element_is_visible()
        self.email_input_field.input_text(Config().APP_LOGIN)


    def input_password(self):
        self.password_input_field.wait_element_is_visible()
        self.password_input_field.input_text(Config().APP_PASSWORD)

    def login(self):
        self.login_button.wait_element_is_visible()
        self.login_button.click_button()
   
