from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.data import card_number, card_code, message_for_driver
from utils import helpers


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_button = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Siguiente']")
    payment_method = (By.CSS_SELECTOR, '.pp-value arrow')
    add_card = (By.XPATH, '//div[@class="pp-tittle" and text()="Agregar tarjeta"]')
    add_card_number = (By.CSS_SELECTOR, 'card-number.input')
    add_card_code = (By.CSS_SELECTOR, 'card-code')
    submit_button = (By.XPATH, "//button[text()='Agregar']")
    close_button = (By.CSS_SELECTOR, '.close.button.section-close')
    driver_message_field = (By.ID, 'comment')
    order_requirements_1 = (By.CSS_SELECTOR, '.switch')
    order_requirements_2 = (By.CSS_SELECTOR, '.counter-plus')
    order_taxi = (By.XPATH, '//div[@class="smart-button-main" and text()="Pedir un taxi"]')

# Route

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# Taxi request
    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

# Comfort request
    def get_comfort_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_icon))

    def click_on_comfort_icon(self):
        self.get_comfort_icon().click()

# Phone number
    def get_phone_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_button))

    def click_on_phone_button(self):
        self.get_phone_button().click()

    def get_phone_number_field(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def type_phone_number_field(self, phone_number):
        self.wait.until(EC.presence_of_element_located(self.phone_number_field)).send_keys(phone_number)

    def get_next_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_button))

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_phone_code_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_code_field))

    def set_phone_code(self, driver):
        code = helpers.retrieve_phone_code(driver)
        self.get_phone_code_field().send_keys(code)

    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_button))

    def click_on_confirm_button(self):
        self.get_confirm_button().click()

# Add Card
    def get_payment_method(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method))

    def click_on_payment_method(self):
        self.get_payment_method().click()

    def get_add_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card))

    def click_on_add_card(self):
        self.get_add_card().click()

    def get_add_card_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_number)).get_property('value')

    def type_add_card_number(self):
        self.wait.until(EC.presence_of_element_located(self.phone_number_field)).send_keys(card_number)

    def get_add_card_code(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_code)).get_property('value')

    def type_add_card_code(self):
        self.wait.until(EC.presence_of_element_located(self.phone_number_field)).send_keys(card_code)

    def get_submit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.submit_button))

    def click_on_submit_button(self):
        self.get_submit_button().click()

    def get_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_button))

    def click_on_close_button(self):
        self.get_close_button().click()
# Message for driver

    def get_driver_message_field(self):
        return self.driver.find_element(*self.driver_message_field).get_property('value')

    def type_driver_message_field(self):
        self.wait.until(EC.presence_of_element_located(self.driver_message_field)).send_keys(message_for_driver)

# Order requirements

    def get_order_requirements_1(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_requirements_1))

    def click_on_order_requirements_1(self):
            self.get_order_requirements_1().click()

    def get_order_requirements_2(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_requirements_2))

    def click_on_order_requirements_2(self):
        self.get_order_requirements_2().click()

# Order taxi

    def get_order_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi))

    def click_on_order_taxi(self):
            self.get_order_taxi().click()




#Getter, Setter, Reader, Clicker