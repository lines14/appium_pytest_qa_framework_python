from main.base_screen import BaseForm
from selenium.webdriver.common.by import By
from main.elements.base_element_children.button import Button

class BrowserWindowsPage(BaseForm):
    def __init__(self):
        super().__init__(By.XPATH, '//div[@class="main-header" and text()="Browser Windows"]', 'page with "browser windows" form')
        self.new_tab_button = Button(By.XPATH, '//*[@id="tabButton"]', '"new tab" button')

    def click_new_tab_button(self):
        self.new_tab_button.click_button()