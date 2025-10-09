from main.utils.log.logger import Logger
from selenium.webdriver.common.keys import Keys
from main.utils.wait.wait_utils import WaitUtils
from main.driver.driver_factory import BrowserFactory

class BaseElement:
    def __init__(self, locator_type, element_locator, element_name):
        self.locator_type = locator_type
        self.element_locator = element_locator
        self.element_name = element_name

    def get_element(self):
        return BrowserFactory.instance.find_element(self.locator_type, self.element_locator)

    def get_elements(self):
        return BrowserFactory.instance.find_elements(self.locator_type, self.element_locator)

    def get_text(self):
        Logger.log(f'[info] ▶ get {self.element_name} text:')
        text = (self.get_element()).text
        Logger.log(f'[info]   text contains: "{text}"')
        return text

    def click_button(self):
        Logger.log(f'[info] ▶ click {self.element_name}')
        (self.get_element()).click()

    def input_text(self, text):
        Logger.log(f'[info] ▶ input {self.element_name}')
        (self.get_element()).send_keys(text)

    def enter_text(self, text):
        Logger.log(f'[info] ▶ input {self.element_name} and submit')
        (self.get_element()).send_keys(text + Keys.ENTER)

    def get_attribute_value(self, attr):
        Logger.log(f'[info] ▶ get {self.element_name} attribute {attr} value:')
        attr_value = (self.get_element()).get_attribute(attr)
        Logger.log(f'[info]   attribute value is: "{attr_value}"')
        return attr_value

    def element_is_displayed(self):
        Logger.log(f'[info] ▶ {self.element_name} is present')
        return (self.get_element()).is_displayed()

    def element_is_enabled(self):
        Logger.log(f'[info] ▶ {self.element_name} is enable')
        return (self.get_element()).is_enabled()

    def parse_children_for_attr(self, attr):
        return list(map(lambda element: element.get_attribute(attr), self.get_elements()))

    def parse_children_for_text(self):
        return list(map(lambda element: element.text, self.get_elements()))

    def wait_is_visible(self):
        Logger.log(f'[info] ▶ wait {self.element_name} is visible')
        WaitUtils.wait_element_visible(self.locator_type, self.element_locator)

    def wait_staleness_of(self):
        WaitUtils.wait_element_staleness_of(self.locator_type, self.element_locator)
    
    def wait_is_clickable(self):
        Logger.log(f'[info] ▶ wait {self.element_name} is clickable')
        WaitUtils.wait_element_clickable(self.locator_type, self.element_locator)
        