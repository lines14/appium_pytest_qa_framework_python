from main.base_form import BaseForm
from selenium.webdriver.common.by import By
from main.elements.base_element_children.button import Button

class LeftMenuForm(BaseForm):
    def __init__(self):
        self.browser_windows_button = Button(By.XPATH, '//span[contains(text(), "Browser Windows")]', '"browser windows" button')
        self.elements_button = Button(By.XPATH, '//div[@class="header-text" and text()="Elements"]', '"elements" button')
        self.links_button = Button(By.XPATH, '//*[@id="item-5"]', '"links" button')

    def click_browser_windows_button(self):
        self.browser_windows_button.click_button()

    def click_elements_button(self):
        self.elements_button.click_button()

    def wait_links_button_visible(self):
        self.links_button.wait_is_visible()

    def click_links_button(self):
        self.links_button.click_button()