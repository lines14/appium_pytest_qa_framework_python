import os
from typing import Optional
from types import SimpleNamespace
from pydantic import model_validator
from main.utils.data.data_utils import DataUtils
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    ADB_PATH: Optional[str] = None
    APPIUM_HOST: str
    APPIUM_PORT: int
    EMULATOR_HOST: str
    EMULATOR_PORT: int

    AUTH_LOGIN: str
    AUTH_PASSWORD: str
    API_BASE_URL: str
    WAIT_TIME: int

    APP: str
    PLATFORM_NAME: str
    AUTOMATION_NAME: str
    DEVICE_NAME: str
    NO_RESET: bool
    FULL_RESET: bool
    NEW_COMMAND_TIMEOUT: int
    CONNECT_HARDWARE_KEYBOARD: bool
    AUTO_WEBVIEW: bool
    AUTO_GRANT_PERMISSIONS: bool
    SETTINGS_WAIT_TIMEOUT: int
    IGNORE_HIDDEN_API_POLICY_ERROR: bool

    APP_PACKAGE: str
    APP_ACTIVITY: str
    ENSURE_WEBVIEWS_HAVE_PAGES: bool
    NATIVE_WEB_SCREENSHOT: bool
    CHROMEDRIVER_AUTODOWNLOAD: bool

    PLATFORM_VERSION: str
    BUNDLE_ID: str
    USE_NEW_WDA: bool
    WDA_LAUNCH_TIMEOUT: int
    WDA_CONNECTION_TIMEOUT: int
    AUTO_ACCEPT_ALERTS: bool
    INCLUDE_SAFARI_IN_WEBVIEWS: bool
    SHOW_XCODE_LOG: bool

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.test"))

    @property
    def DB_URL_ASYNC(self) -> str:
        return (f"mysql+aiomysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
    
    @property
    def DB_URL_SYNC(self) -> str:
        return (f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
    
    @property
    def APPIUM_URL(self) -> str:
        return f"http://{self.APPIUM_HOST}:{self.APPIUM_PORT}"

    # change if custom ADB connection
    @property
    def UDID(self) -> str:
        # return f"{self.EMULATOR_HOST}:{self.EMULATOR_PORT}"
        return self.DEVICE_NAME

    @property
    def USER(self):
        return SimpleNamespace(
            login=self.AUTH_LOGIN,
            password=self.AUTH_PASSWORD,
        )
    
    @property
    def ANDROID_CAPABILITIES(self):
        instance = SimpleNamespace(
            udid=self.UDID,
            app=self.APP,
            platformName=self.PLATFORM_NAME,
            deviceName=self.UDID,
            automationName=self.AUTOMATION_NAME,
            noReset=self.NO_RESET,
            newCommandTimeout=self.NEW_COMMAND_TIMEOUT,
            ignoreHiddenApiPolicyError=self.IGNORE_HIDDEN_API_POLICY_ERROR,
        
            appPackage=self.APP_PACKAGE,
            appActivity=self.APP_ACTIVITY,
            ensureWebviewsHavePages=self.ENSURE_WEBVIEWS_HAVE_PAGES,
            nativeWebScreenshot=self.NATIVE_WEB_SCREENSHOT
        )

        setattr(instance, "appium:fullReset", self.FULL_RESET)
        setattr(instance, 'appium:autoWebview', self.AUTO_WEBVIEW)
        setattr(instance, "appium:settings[waitTimeout]", self.SETTINGS_WAIT_TIMEOUT)
        setattr(instance, "appium:autoGrantPermissions", self.AUTO_GRANT_PERMISSIONS)
        setattr(instance, 'appium:connectHardwareKeyboard', self.CONNECT_HARDWARE_KEYBOARD)
        setattr(instance, 'appium:chromedriver_autodownload', self.CHROMEDRIVER_AUTODOWNLOAD)
        return instance

    @property
    def IOS_CAPABILITIES(self):
        instance = SimpleNamespace(
            udid=self.UDID,
            app=self.APP,
            platformName=self.PLATFORM_NAME,
            deviceName=self.UDID,
            automationName=self.AUTOMATION_NAME,
            noReset=self.NO_RESET,
            newCommandTimeout=self.NEW_COMMAND_TIMEOUT,
            ignoreHiddenApiPolicyError=self.IGNORE_HIDDEN_API_POLICY_ERROR,
        
            platformVersion=self.PLATFORM_VERSION,
            bundleId=self.BUNDLE_ID,
            useNewWDA=self.USE_NEW_WDA,
            wdaLaunchTimeout=self.WDA_LAUNCH_TIMEOUT,
            wdaConnectionTimeout=self.WDA_CONNECTION_TIMEOUT,
            autoAcceptAlerts=self.AUTO_ACCEPT_ALERTS,
            includeSafariInWebviews=self.INCLUDE_SAFARI_IN_WEBVIEWS,
            showXcodeLog=self.SHOW_XCODE_LOG
        )

        setattr(instance, "appium:fullReset", self.FULL_RESET)
        setattr(instance, 'appium:autoWebview', self.AUTO_WEBVIEW)
        setattr(instance, "appium:settings[waitTimeout]", self.SETTINGS_WAIT_TIMEOUT)
        setattr(instance, "appium:autoGrantPermissions", self.AUTO_GRANT_PERMISSIONS)
        setattr(instance, 'appium:connectHardwareKeyboard', self.CONNECT_HARDWARE_KEYBOARD)
        return instance

    @model_validator(mode="after")
    def fill_adb_path(self):
        if not self.ADB_PATH:
            self.ADB_PATH = os.path.join(
                DataUtils.dict_to_model(dict(os.environ)).ANDROID_HOME, 
                "platform-tools/adb"
            )
            
        return self