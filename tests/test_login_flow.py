import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "appPackage": "kz.adp.app",
        "appActivity": "kz.adp.app.MainActivity",
        "noReset": False,
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        "newCommandTimeout": 3600,
        "connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://172.25.48.1:4723", options=options)
    yield driver
    driver.quit()


def test_forgot_password_disabled_button(driver):
    wait = WebDriverWait(driver, 15)

    allow_btn = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Allow']"))
    )
    allow_btn.click()

    login_btn = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Вход']"))
    )
    login_btn.click()

    webview_context = next(ctx for ctx in driver.contexts if "WEBVIEW" in ctx)
    driver.switch_to.context(webview_context)

    driver.execute_script("""
        const btn = [...document.querySelectorAll('button')]
            .find(el => el.innerText.trim() === 'По email');
        if (btn) btn.click();
    """)

    driver.switch_to.context("NATIVE_APP")
    forgot_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Забыли пароль?']")
    forgot_btn.click()

    driver.switch_to.context(webview_context)
    send_code_btn = driver.find_element(AppiumBy.XPATH, "//button[contains(., 'Выслать код')]")
    assert not send_code_btn.is_enabled(), "Ожидалось, что кнопка 'Выслать код' будет неактивной при пустом email"