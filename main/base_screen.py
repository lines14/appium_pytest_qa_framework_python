from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils
from main.driver.driver_factory import DriverFactory

class BaseScreen:
    def __init__(self, locator_type, screen_locator, screen_name):
        self.locator_type = locator_type
        self.screen_locator = screen_locator
        self.screen_name = screen_name

    def get_unique_element(self):
        return DriverFactory.instance.find_element(self.locator_type, self.screen_locator)

    def check_screen_is_displayed(self):
        Logger.log(f'[info] ▶ {self.screen_name} is displayed')
        return (self.get_unique_element()).is_displayed()

    def check_screen_is_enabled(self):
        Logger.log(f'[info] ▶ {self.screen_name} is enabled')
        return (self.get_unique_element()).is_enabled()
    
    def wait_screen_is_visible(self):
        Logger.log(f'[info] ▶ wait {self.screen_name} is visible')
        WaitUtils.wait_element_visible(self.locator_type, self.screen_locator)
    
    def wait_screen_is_clickable(self):
        Logger.log(f'[info] ▶ wait {self.screen_name} is clickable')
        WaitUtils.wait_element_clickable(self.locator_type, self.screen_locator)