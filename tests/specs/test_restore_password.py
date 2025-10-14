import pytest
from main.driver.driver_utils import DriverUtils
from tests.screen_objects import StartScreen, LoginScreen, ForgotPasswordScreen


class TestRestorePassword:
    @pytest.mark.asyncio
    async def test_restore_password(self):
        start_screen = StartScreen()
        login_screen = LoginScreen()
        forgot_password_screen = ForgotPasswordScreen()

        start_screen.wait_screen_is_visible()
        start_screen.click_login_button()
        DriverUtils.switch_to_webview_context()
        start_screen.click_by_email_button()

        DriverUtils.switch_to_native_context()
        login_screen.wait_screen_is_visible()
        login_screen.click_forgot_password_button()

        DriverUtils.switch_to_webview_context()
        forgot_password_screen.wait_screen_is_visible()
        assert not forgot_password_screen.send_code_button_is_enabled(), "Кнопка 'Выслать код' неактивна при пустом email"