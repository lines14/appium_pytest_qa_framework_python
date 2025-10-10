from config import Config
from main.driver.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WaitUtils:
    @staticmethod
    def _wait_until(condition):
        return WebDriverWait(DriverFactory.instance, Config().WAIT_TIME).until(condition)

    @classmethod
    def wait_new_window_is_opened_in_webview(cls, prev_tabs_list):
        return cls._wait_until(expected_conditions.new_window_is_opened(prev_tabs_list))

    @classmethod
    def wait_alert_is_present_in_webview(cls):
        return cls._wait_until(expected_conditions.alert_is_present())
    
    @classmethod
    def wait_element_located(cls, locator_type, locator):
        return cls._wait_until(expected_conditions.presence_of_element_located((locator_type, locator)))

    @classmethod
    def wait_element_visible(cls, locator_type, locator):
        return cls._wait_until(expected_conditions.visibility_of_element_located((locator_type, locator)))

    @classmethod
    def wait_element_staleness_of(cls, element):
        return cls._wait_until(expected_conditions.staleness_of(element))

    @classmethod
    def wait_element_clickable(cls, locator_type, locator):
        return cls._wait_until(expected_conditions.element_to_be_clickable((locator_type, locator)))