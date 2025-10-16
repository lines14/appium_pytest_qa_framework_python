from main.utils.log.logger import Logger
from selenium.webdriver.common.keys import Keys
from main.utils.wait.wait_utils import WaitUtils
from main.driver.driver_factory import DriverFactory
from appium.webdriver.common.appiumby import AppiumBy

class BaseElement:
    def __init__(self, locator_type, element_locator, element_name):
        self.locator_type = locator_type
        self.element_locator = element_locator
        self.element_name = element_name

    def get_element(self):
        if self.locator_type == AppiumBy.ANDROID_UIAUTOMATOR:
            element_locator = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({self.element_locator})'
            return DriverFactory.instance.find_element(self.locator_type, element_locator)
        else:
            return DriverFactory.instance.find_element(self.locator_type, self.element_locator)

    def get_elements(self):
        return DriverFactory.instance.find_elements(self.locator_type, self.element_locator)

    def get_text(self):
        Logger.log(f'[inf] ▶ get {self.element_name} text:')
        text = (self.get_element()).text
        Logger.log(f'[inf]   text contains: "{text}"')
        return text

    def click_button(self):
        Logger.log(f'[inf] ▶ click {self.element_name}')
        (self.get_element()).click()

    def tap(self):
        DriverFactory.instance.execute_script("mobile: clickGesture", {"elementId": (self.get_element()).id})

    def input_text(self, text):
        Logger.log(f'[inf] ▶ input {self.element_name}')
        element = self.get_element()
        element.clear()
        element.send_keys(text)

    def enter_text_in_webview(self, text):
        Logger.log(f'[inf] ▶ input {self.element_name} and submit')
        (self.get_element()).send_keys(text + Keys.ENTER)

    def get_attribute_value(self, attr):
        Logger.log(f'[inf] ▶ get {self.element_name} attribute {attr} value:')
        attr_value = (self.get_element()).get_attribute(attr)
        Logger.log(f'[inf]   attribute value is: "{attr_value}"')
        return attr_value

    def check_element_is_displayed(self):
        Logger.log(f'[inf] ▶ check {self.element_name} is displayed')
        return (self.get_element()).is_displayed()

    def check_element_is_enabled(self):
        Logger.log(f'[inf] ▶ check {self.element_name} is enabled')
        return (self.get_element()).is_enabled()

    def parse_children_for_attr(self, attr):
        return list(map(lambda element: element.get_attribute(attr), self.get_elements()))

    def parse_children_for_text(self):
        return list(map(lambda element: element.text, self.get_elements()))

    def wait_element_is_located(self):
        Logger.log(f'[inf] ▶ wait {self.element_name} is located')
        WaitUtils.wait_element_located(self.locator_type, self.element_locator)

    def wait_element_is_visible(self):
        Logger.log(f'[inf] ▶ wait {self.element_name} is visible')
        WaitUtils.wait_element_visible(self.locator_type, self.element_locator)

    def wait_staleness_of_element(self):
        Logger.log(f'[inf] ▶ wait staleness of {self.element_name}')
        WaitUtils.wait_element_staleness_of(self.locator_type, self.element_locator)
    
    def wait_element_is_clickable(self):
        Logger.log(f'[inf] ▶ wait {self.element_name} is clickable')
        WaitUtils.wait_element_clickable(self.locator_type, self.element_locator)