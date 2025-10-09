from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils
from main.driver.driver_factory import BrowserFactory

class BaseForm:
    def __init__(self, locator_type, page_locator, page_name):
        self.locator_type = locator_type
        self.page_locator = page_locator
        self.page_name = page_name

    def get_unique_element(self):
        return BrowserFactory.instance.find_element(self.locator_type, self.page_locator)

    def page_is_displayed(self):
        Logger.log(f'[info] ▶ {self.page_name} is open')
        return (self.get_unique_element()).is_displayed()

    def page_is_enabled(self):
        Logger.log(f'[info] ▶ {self.page_name} is enable')
        return (self.get_unique_element()).is_enabled()
    
    def wait_page_is_visible(self):
        WaitUtils.wait_element_visible(self.locator_type, self.page_locator)
    
    def wait_page_is_clickable(self):
        WaitUtils.wait_element_clickable(self.locator_type, self.page_locator)