from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils
from main.driver.driver_factory import DriverFactory
from appium.webdriver.common.touch_action import TouchAction

class DriverUtils:
    @staticmethod
    def init_the_driver():
        Logger.log('[info] ▶ init driver')
        DriverFactory.init_instance()

    @staticmethod
    def scroll_to_the_bottom_in_webview():
        DriverFactory.instance.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    @staticmethod
    def handle_original_tab_in_webview():
        return DriverFactory.instance.current_window_handle
    
    @staticmethod
    def get_tabs_list_in_webview():
        return DriverFactory.instance.window_handles

    @staticmethod
    def switch_driver_to_another_tab_in_webview(prev_tabs_list, original_window):
        Logger.log(f'[info] ▶ switch driver to another tab')
        WaitUtils.wait_new_window_is_opened_in_webview(prev_tabs_list)
        for window_handle in DriverFactory.instance.window_handles:
            if window_handle != original_window:
                DriverFactory.instance.switch_to.window(window_handle)
                break

    @staticmethod
    def switch_driver_to_original_tab_in_webview(original_tab):
        Logger.log('[info] ▶ switch driver to previous tab')
        DriverFactory.instance.switch_to.window(original_tab)

    @staticmethod
    def get_alert_in_webview():
        return WaitUtils.wait_alert_is_present_in_webview()

    @classmethod
    def get_alert_text_in_webview(cls):
        Logger.log('[info] ▶ alert with text is open')
        text = (cls.get_alert_in_webview()).text
        Logger.log(f'[info]   text contains: "{text}"')
        return text

    @classmethod
    def enter_text_to_alert_in_webview(cls, text):
        Logger.log('[info] ▶ input text to alert form')
        (cls.get_alert_in_webview()).send_keys(text)

    @classmethod
    def accept_alert_in_webview(cls):
        Logger.log('[info] ▶ accept alert')
        (cls.get_alert_in_webview()).accept()

    @classmethod
    def alert_is_displayed_in_webview(cls):
        try:
            cls.get_alert_in_webview()
            return True
        except:
            return False

    @staticmethod
    def go_into_frame_in_webview(id_or_index):
        Logger.log('[info] ▶ go into frame')
        DriverFactory.instance.switch_to.frame(id_or_index)

    @staticmethod
    def go_out_of_frame_in_webview():
        Logger.log('[info] ▶ go out of frame')
        DriverFactory.instance.switch_to.default_content()

    @staticmethod
    def close_tab_in_webview():
        Logger.log('[info] ▶ close tab')
        DriverFactory.instance.close()

    @staticmethod
    def tap(self):
        Logger.log(f'[info] ▶ tap {self.element_name}')
        TouchAction(DriverFactory.instance).tap(self.get_element()).perform()

    @staticmethod
    def get_context(substr):
        return next(ctx for ctx in DriverFactory.instance.contexts if substr in ctx)

    @classmethod
    def switch_to_webview_context(cls):
        DriverFactory.instance.switch_to.context(cls.get_context('WEBVIEW'))

    @classmethod
    def switch_to_native_context(cls):
        DriverFactory.instance.switch_to.context(cls.get_context('NATIVE_APP'))
    
    @staticmethod
    def quit_driver():
        Logger.log('[info] ▶ quit driver')
        DriverFactory.instance.quit()
        DriverFactory.instance = None