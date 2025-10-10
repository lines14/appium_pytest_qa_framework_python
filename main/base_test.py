from tests.DB.project_DB import ProjectDB
from main.driver.driver_utils import DriverUtils
from main.utils.log.logger import Logger

class BaseTest:
    project_DB = ProjectDB()

    @classmethod
    def setup_class(cls):
        cls.project_DB.create_connection()
        DriverUtils.init_the_driver()

    @classmethod
    def teardown_class(cls):
        DriverUtils.quit_driver()
        cls.project_DB.close_connection()
        Logger.log_to_file()