from config import Config
from main.driver.emulator_utils import EmulatorUtils
from main.driver.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WaitUtils:
    @staticmethod
    def __wait_until(condition, before_driver_init=False):
        driver = None

        if not before_driver_init:
            driver = DriverFactory.instance

        return WebDriverWait(driver, Config().WAIT_TIME).until(condition)

    @classmethod
    def wait_adb_device(cls):
        cls.__wait_until(lambda _: EmulatorUtils.is_adb_device_exists(), before_driver_init=True) 

    @classmethod
    def wait_activity_manager_ready(cls):
        cls.__wait_until(lambda _: EmulatorUtils.is_activity_manager_ready(), before_driver_init=True)
    
    @classmethod
    def wait_android_emulator_ready(cls):
        cls.__wait_until(lambda _: EmulatorUtils.is_android_emulator_ready(), before_driver_init=True) 

    @classmethod
    def wait_new_window_is_opened_in_webview(cls, prev_tabs_list):
        return cls.__wait_until(expected_conditions.new_window_is_opened(prev_tabs_list))

    @classmethod
    def wait_alert_is_present_in_webview(cls):
        return cls.__wait_until(expected_conditions.alert_is_present())
    
    @classmethod
    def wait_element_located(cls, locator_type, locator):
        return cls.__wait_until(expected_conditions.presence_of_element_located((locator_type, locator)))

    @classmethod
    def wait_element_visible(cls, locator_type, locator):
        return cls.__wait_until(expected_conditions.visibility_of_element_located((locator_type, locator)))

    @classmethod
    def wait_element_staleness_of(cls, element):
        return cls.__wait_until(expected_conditions.staleness_of(element))

    @classmethod
    def wait_element_clickable(cls, locator_type, locator):
        return cls.__wait_until(expected_conditions.element_to_be_clickable((locator_type, locator)))