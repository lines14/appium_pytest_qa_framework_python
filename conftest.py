import pytest
from tests.API.auth_API import AuthAPI
from main.utils.DB.base_DB import BaseDB
from main.utils.log.logger import Logger
from main.driver.driver_utils import DriverUtils
from main.driver.driver_factory import DriverFactory


@pytest.fixture(scope="function", autouse=True)
async def setup_and_teardown():
    base_DB = BaseDB()
    await base_DB.init_tables()
    await AuthAPI().set_token()
    DriverUtils.init_the_driver()

    yield DriverFactory.instance

    DriverUtils.quit_driver()
    await base_DB.dispose_engine()
    Logger.log_to_file()