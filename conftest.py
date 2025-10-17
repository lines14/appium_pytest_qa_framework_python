import pytest
from tests.API.auth_API import AuthAPI
from main.utils.log.logger import Logger
# from main.utils.DB.base_DB import BaseDB
from tests.screen_objects import SystemAlerts
from main.driver.driver_utils import DriverUtils
from main.driver.driver_factory import DriverFactory


@pytest.fixture(scope="function", autouse=True)
async def setup_and_teardown():
    # base_DB = BaseDB()
    system_alerts = SystemAlerts()

    # await base_DB.init_tables()
    await AuthAPI().set_token()
    DriverUtils.init_the_driver()

    if system_alerts.system_alert_close_button_is_displayed():
        system_alerts.click_system_alert_close_button()

    # yield DriverFactory.instance

    DriverUtils.quit_driver()
    # await base_DB.dispose_engine()
    Logger.log_to_file()