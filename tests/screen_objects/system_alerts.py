from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button

class SystemAlerts(BaseScreen):
    def __init__(self):
        self.system_alert_close_button = Button(AppiumBy.XPATH, '//android.widget.TextView[@text="Close app"]', 'system alert close button')

    def system_alert_close_button_is_displayed(self):
        try:
            return self.system_alert_close_button.element_is_displayed()
        except:
            return False

    def click_system_alert_close_button(self):
        self.system_alert_close_button.click_button()