from main.base_form import BaseForm
from selenium.webdriver.common.by import By
from main.elements.base_element_children.button import Button

class MainPage(BaseForm):
    def __init__(self):
        super().__init__(By.XPATH, '//*[@id="app"]//following-sibling::img[@class="banner-image"]', 'main page')
        self.alerts_frame_windows_button = Button(By.XPATH, '//h5[contains(text(), "Alerts, Frame & Windows")]', '"alerts, frame & windows" button')

    def click_alerts_frame_windows_button(self):
        self.alerts_frame_windows_button.click_button()