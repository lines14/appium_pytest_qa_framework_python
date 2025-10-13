import os
from types import SimpleNamespace
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    APPIUM_HOST: str
    APPIUM_PORT: int

    AUTH_LOGIN: str
    AUTH_PASSWORD: str
    API_BASE_URL: str
    WAIT_TIME: int

    APP: str
    PLATFORM_NAME: str
    DEVICE_NAME: str
    AUTOMATION_NAME: str
    NO_RESET: bool
    FULL_RESET: bool
    NEW_COMMAND_TIMEOUT: int
    CONNECT_HARDWARE_KEYBOARD: bool
    AUTO_WEBVIEW: bool
    AUTO_GRANT_PERMISSIONS: bool

    APP_PACKAGE: str
    APP_ACTIVITY: str
    ENSURE_WEBVIEWS_HAVE_PAGES: bool
    NATIVE_WEB_SCREENSHOT: bool
    CHROMEDRIVER_AUTODOWNLOAD: bool

    PLATFORM_VERSION: str
    BUNDLE_ID: str
    UDID: str
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

    @property
    def USER(self):
        return SimpleNamespace(
            login=self.AUTH_LOGIN,
            password=self.AUTH_PASSWORD,
        )
    
    @property
    def ANDROID_CAPABILITIES(self):
        instance = SimpleNamespace(
            app=self.APP,
            platformName=self.PLATFORM_NAME,
            deviceName=self.DEVICE_NAME,
            automationName=self.AUTOMATION_NAME,
            noReset=self.NO_RESET,
            newCommandTimeout=self.NEW_COMMAND_TIMEOUT,
            connectHardwareKeyboard=self.CONNECT_HARDWARE_KEYBOARD,
        
            appPackage=self.APP_PACKAGE,
            appActivity=self.APP_ACTIVITY,
            ensureWebviewsHavePages=self.ENSURE_WEBVIEWS_HAVE_PAGES,
            nativeWebScreenshot=self.NATIVE_WEB_SCREENSHOT
        )

        setattr(instance, "appium:fullReset", self.FULL_RESET)
        setattr(instance, 'appium:autoWebview', self.AUTO_WEBVIEW)
        setattr(instance, "appium:autoGrantPermissions", self.AUTO_GRANT_PERMISSIONS)
        setattr(instance, 'appium:chromedriverAutodownload', self.CHROMEDRIVER_AUTODOWNLOAD)
        return instance

    @property
    def IOS_CAPABILITIES(self):
        instance = SimpleNamespace(
            app=self.APP,
            platformName=self.PLATFORM_NAME,
            deviceName=self.DEVICE_NAME,
            automationName=self.AUTOMATION_NAME,
            noReset=self.NO_RESET,
            newCommandTimeout=self.NEW_COMMAND_TIMEOUT,
            connectHardwareKeyboard=self.CONNECT_HARDWARE_KEYBOARD,
        
            platformVersion=self.PLATFORM_VERSION,
            bundleId=self.BUNDLE_ID,
            udid=self.UDID,
            useNewWDA=self.USE_NEW_WDA,
            wdaLaunchTimeout=self.WDA_LAUNCH_TIMEOUT,
            wdaConnectionTimeout=self.WDA_CONNECTION_TIMEOUT,
            autoAcceptAlerts=self.AUTO_ACCEPT_ALERTS,
            includeSafariInWebviews=self.INCLUDE_SAFARI_IN_WEBVIEWS,
            showXcodeLog=self.SHOW_XCODE_LOG
        )

        setattr(instance, "appium:fullReset", self.FULL_RESET)
        setattr(instance, 'appium:autoWebview', self.AUTO_WEBVIEW)
        setattr(instance, "appium:autoGrantPermissions", self.AUTO_GRANT_PERMISSIONS)
        return instance