from main.base_form import BaseForm
from selenium.webdriver.common.by import By
from main.elements.base_element_children.label import Label

class LinksPage(BaseForm):
    def __init__(self):
        super().__init__(By.XPATH, '//div[@class="main-header" and text()="Links"]', 'page with "links" form')
        self.home_link = Label(By.XPATH, '//*[@id="simpleLink"]', '"home" link')

    def click_home_link(self):
        self.home_link.click_button()