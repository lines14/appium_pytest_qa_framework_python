from tests.DB.project_DB import ProjectDB
from main.driver.driver_utils import BrowserUtils
from main.utils.log.logger import Logger

class BaseTest:
    project_DB = ProjectDB()

    @classmethod
    def setup_class(cls):
        cls.project_DB.create_connection()
        BrowserUtils.init_the_driver()

    @classmethod
    def teardown_class(cls):
        BrowserUtils.quit_driver()
        cls.project_DB.close_connection()
        Logger.log_to_file()