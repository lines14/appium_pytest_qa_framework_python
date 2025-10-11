from main.base_screen import BaseForm
from selenium.webdriver.common.by import By

class SamplePage(BaseForm):
    def __init__(self):
        super().__init__(By.XPATH, '//*[text()="This is a sample page"]', 'new tab with sample page')