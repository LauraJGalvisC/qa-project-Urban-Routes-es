import time
from data import data
from pages import urban_routes_page as urp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import helpers


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        #self.driver.get(data.urban_routes_url)
        #routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort(self):
        self.routes_page.click_on_request_taxi_button()
        self.routes_page.click_on_comfort_icon()
        time.sleep(10)

    def test_phone_number(self):
        self.routes_page.click_on_phone_button()
        self.routes_page.type_phone_number_field(data.phone_number)
        self.routes_page.click_on_next_button()
        self.routes_page.set_phone_code(self.driver)
        self.routes_page.click_on_confirm_button(self.driver)
        self.routes_page.click_on_payment_method()
        self.routes_page.type_add_card_number()
        self.routes_page.type_add_card_number()
        self.routes_page.click_on_submit_button()
        self.routes_page.click_on_close_button()
        self.routes_page.type_driver_message_field()
        self.routes_page.click_on_order_requirements_1()
        self.routes_page.click_on_order_requirements_2()
        self.routes_page.click_on_order_taxi()
        time.sleep(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

