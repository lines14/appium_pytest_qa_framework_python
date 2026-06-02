import pytest
from main.driver.driver_utils import DriverUtils
from tests.screen_objects import StartScreen, HomeScreen


class TestLoginAsAgentAndIssuePolicy:
    @pytest.mark.asyncio
    async def test_login_as_agent(self):
        start_screen = StartScreen()
        home_screen = HomeScreen()


        start_screen.wait_screen_is_visible()
        DriverUtils.switch_to_native_context()
        start_screen.click_sign_in_button()
        DriverUtils.switch_to_webview_context()
        start_screen.click_by_email_button()
        DriverUtils.switch_to_native_context()
        start_screen.input_email()
        start_screen.input_password()
        start_screen.login()

        home_screen.wait_screen_is_visible()
        home_screen.create_new_policy()
        home_screen.select_countries()
        home_screen.pick_trip_date()




