from main.base_screen import BaseForm
from selenium.webdriver.common.by import By

class AlertsFrameWindowsPage(BaseForm):
    def __init__(self):
        super().__init__(By.XPATH, '//div[@class="main-header" and text()="Alerts, Frame & Windows"]', '"alerts, frame & windows" page')