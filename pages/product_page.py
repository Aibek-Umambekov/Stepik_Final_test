from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_added_to_basket_message(self):
        added_message = self.browser.find_element(*ProductPageLocators.BASKET_ADDED_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert added_message == product_name, "Product name in message doesn't match"

    def should_be_basket_cost_message(self):
        basket_cost_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in basket_cost_message, "Product price is not in the basket cost message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_ADDED_MESSAGE), \
            "Success message should disappear, but it's still present"

