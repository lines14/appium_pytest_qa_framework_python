import pytest
from main.driver.driver_factory import DriverFactory
from tests.screen_objects import StartScreen, LoginScreen, ForgotPasswordScreen


class TestRestorePassword:
    @pytest.mark.asyncio
    async def test_restore_password(self):
        start_screen = StartScreen()
        login_screen = LoginScreen()
        forgot_password_screen = ForgotPasswordScreen()

        start_screen.wait_screen_is_visible()

        start_screen.click_login_button()

        start_screen.wait_by_email_button_visible()
        start_screen.click_by_email_button()

        login_screen.wait_screen_is_visible()
        login_screen.click_forgot_password_button()

        webview_context = next(ctx for ctx in DriverFactory.instance.contexts if "WEBVIEW" in ctx)
        DriverFactory.instance.switch_to.context(webview_context)

        forgot_password_screen.wait_screen_is_visible()
        assert not forgot_password_screen.send_code_button_is_enabled(), "Кнопка 'Выслать код' неактивна при пустом email"