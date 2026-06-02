from main.base_screen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy
from main.elements.base_elements.button import Button
from main.elements.base_elements.text_box import TextBox



class HomeScreen(BaseScreen):
    def __init__(self):
        super().__init__(AppiumBy.XPATH, '//android.widget.TextView[@text="Полисы"]', 'home screen') # compatible with older api-levels
        self.new_policy = Button(AppiumBy.XPATH, '//android.widget.Button[@text="+ Новый полис"]', 'new policy button')
        self.new_policy_text = TextBox(AppiumBy.XPATH, '//android.widget.TextView[@text="Новый полис МСТ"]', 'new policy text')
        self.countries = Button(AppiumBy.XPATH, '(//android.view.View[@resource-id="main-layout"]/android.widget.Button[@text="Выбрать"])[1]', 'countries button')
        self.countries_text = TextBox(AppiumBy.XPATH, '//android.widget.TextView[@text="Выберите страны"]', 'countries text')
        self.country = Button(AppiumBy.XPATH, '//android.widget.CheckBox[@text=" Германия"]', 'country checkbox')
        self.done_button = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Готово"]', 'done button')
        self.trip_date = Button(AppiumBy.XPATH, '//android.widget.Button[@text="Выбрать"]', 'trip date button')
        self.trip_date_calendar = Button(AppiumBy.XPATH, '(//android.view.View[@text="1"])[2]', 'trip date calendar')
        

    def create_new_policy(self):
        self.new_policy.wait_element_is_visible()
        self.new_policy.click_button()
        self.new_policy_text.wait_element_is_visible()

    def select_countries(self):
        self.countries.wait_element_is_visible()
        self.countries.click_button()
        self.countries_text.wait_element_is_visible()
        self.country.click_button()
        self.done_button.wait_element_is_visible()
        self.done_button.click_button()

    def pick_trip_date(self):
        self.trip_date.wait_element_is_visible()
        self.trip_date.click_button()
        self.trip_date_calendar.wait_element_is_visible()
        self.trip_date_calendar.click_button()


    

    
   
