from assertions import assert_truth
from conftest import BaseTest
from main.utils.data.JSON_loader import JSONLoader
from main.driver.driver_utils import DriverUtils
from tests.page_objects.main_page import MainPage
from tests.page_objects.alerts_frame_windows_page import AlertsFrameWindowsPage
from tests.page_objects.left_menu_form import LeftMenuForm
from tests.page_objects.browser_windows_page import BrowserWindowsPage
from tests.page_objects.sample_page import SamplePage
from tests.page_objects.links_page import LinksPage

class TestUI(BaseTest):
    @staticmethod
    def test_handles():
        main_page = MainPage()
        alerts_frame_windows_page = AlertsFrameWindowsPage()
        left_menu_form = LeftMenuForm()
        browser_windows_page = BrowserWindowsPage()
        sample_page = SamplePage()
        links_page = LinksPage()

        DriverUtils.get_url(JSONLoader.get_config_data().base_URL)
        assert_truth(main_page.page_is_displayed(), 'main page is open')

        main_page.click_alerts_frame_windows_button()
        assert_truth(alerts_frame_windows_page.page_is_displayed(), '"alerts, frame & windows" page is open')
        left_menu_form.click_browser_windows_button()
        assert_truth(browser_windows_page.page_is_displayed(), 'page with "browser windows" form is open')

        original_tab = DriverUtils.handle_original_tab()
        prev_tabs_list = DriverUtils.get_tabs_list()
        browser_windows_page.click_new_tab_button()
        assert_truth(len(DriverUtils.get_tabs_list()) > len(prev_tabs_list), 'new tab is open')
        DriverUtils.switch_driver_to_another_tab(prev_tabs_list, original_tab)
        assert_truth(sample_page.page_is_displayed(), 'sample page is open')

        DriverUtils.close_tab()
        DriverUtils.switch_driver_to_original_tab(original_tab)
        assert_truth(browser_windows_page.page_is_displayed(), 'page with "browser windows" form is open')

        left_menu_form.click_elements_button()
        left_menu_form.wait_links_button_visible()
        left_menu_form.click_links_button()
        assert_truth(links_page.page_is_displayed(), 'page with "links" form is open')

        original_tab = DriverUtils.handle_original_tab()
        prev_tabs_list = DriverUtils.get_tabs_list()
        links_page.click_home_link()
        assert_truth(len(DriverUtils.get_tabs_list()) > len(prev_tabs_list), 'new tab is open')
        DriverUtils.switch_driver_to_another_tab(prev_tabs_list, original_tab)
        assert_truth(main_page.page_is_displayed(), 'main page is open')

        DriverUtils.switch_driver_to_original_tab(original_tab)
        assert_truth(links_page.page_is_displayed(), 'page with "links" form is open')

