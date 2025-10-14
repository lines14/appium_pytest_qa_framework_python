import threading
import classutilities
from config import Config
from appium import webdriver
from appium.options.common import AppiumOptions
from main.utils.data.data_utils import DataUtils

class DriverFactory(classutilities.ClassPropertiesMixin):
    __instance = None
    __lock = threading.Lock()

    @classmethod
    def init_instance(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    from main.utils.wait.wait_utils import WaitUtils
                    options = AppiumOptions()
                    
                    if Config().PLATFORM_NAME == 'Android':
                        WaitUtils.wait_adb_device()
                        WaitUtils.wait_activity_manager_ready()
                        WaitUtils.wait_android_emulator_ready()
                        
                        options.load_capabilities(DataUtils.model_to_dict(Config().ANDROID_CAPABILITIES))
                    elif Config().PLATFORM_NAME == 'iOS':
                        options.load_capabilities(DataUtils.model_to_dict(Config().IOS_CAPABILITIES))

                    cls.__instance = webdriver.Remote(Config().APPIUM_URL, options=options)

    @classutilities.classproperty
    def instance(cls):
        return cls.__instance
        
    @instance.setter
    def instance(cls, value):
        cls.__instance = value