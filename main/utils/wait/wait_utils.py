from main.driver.driver_factory import BrowserFactory
from selenium.webdriver.support.ui import WebDriverWait
from main.utils.data.config_manager import ConfigManager
from selenium.webdriver.support import expected_conditions

class WaitUtils:
    @staticmethod
    def wait_new_window_is_opened(prev_tabs_list):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.new_window_is_opened(prev_tabs_list))

    @staticmethod
    def wait_alert_is_present():
        return WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.alert_is_present())
    
    @staticmethod
    def wait_element_located(locator_type, locator):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.presence_of_element_located((locator_type, locator)))

    @staticmethod
    def wait_element_visible(locator_type, locator):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.visibility_of_element_located((locator_type, locator)))

    @staticmethod
    def wait_element_staleness_of(locator_type, locator):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.staleness_of((locator_type, locator)))

    @staticmethod
    def wait_element_clickable(locator_type, locator):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.element_to_be_clickable((locator_type, locator)))