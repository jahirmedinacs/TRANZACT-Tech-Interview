import string
import random
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def generate_random_char_string(param):
    # Generate random string with length = param
    return ''.join(random.choice(string.ascii_letters) for i in range(param))


def generate_random_number_string(param):
    # Generate random string with length = param
    return ''.join(random.choice(string.digits) for i in range(param))


def generate_random_mixed_string(param):
    # Generate random string with length = param
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(param))


class Task1Page(BasePage):
    # Sign in button
    SIGN_IN_BUTTON = (By.XPATH, "//a[@href=\"/account/login\"]")
    # Create account button
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[@class=\"text-interactive\"]")

    # Full name field
    FULL_NAME_FIELD = (By.XPATH, "//input[@name=\"full_name\"]")
    # Email field
    EMAIL_FIELD = (By.XPATH, "//input[@name=\"email\"]")
    # Password field
    PASSWORD_FIELD = (By.XPATH, "//input[@name=\"password\"]")

    # Sign up button
    SIGN_UP_BUTTON = (By.XPATH, "//button/span")

    # Navigation bar elements
    MEN_NAVIGATION_BAR = (By.XPATH, "//li[@class=\"nav-item\"]//a[@href=\"/category/men\"]")
    KIDS_NAVIGATION_BAR = (By.XPATH, "//li[@class=\"nav-item\"]//a[@href=\"/category/kids\"]")
    WOMEN_NAVIGATION_BAR = (By.XPATH, "//li[@class=\"nav-item\"]//a[@href=\"/category/women\"]")

    NAVIGATION_OPTIONS = [MEN_NAVIGATION_BAR, KIDS_NAVIGATION_BAR, WOMEN_NAVIGATION_BAR]

    # List of products
    PRODUCT_LIST = (By.XPATH, "//div[@class=\"grid grid-cols-2 md:grid-cols-3 gap-2\"]//div[@class=\"listing-tem\"]")

    # Product details
    PRODUCT_DETAILS = (By.XPATH, "//ul[@class=\"variant-option-list flex justify-start\"]")

    # Add to cart button
    ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()=\"ADD TO CART\"]//ancestor::button")

    # Cart button
    CART_BUTTON = (By.XPATH, "//a[@href=\"/cart\"]")

    # Checkout button
    CHECKOUT_BUTTON = (By.XPATH, "//a[@href=\"/checkout\"]")

    # Checkout form
    # Full name field
    FULL_NAME_CHECKOUT_FIELD = (By.XPATH, "//input[@name=\"address[full_name]\"]")
    # Telephone field
    TELEPHONE_CHECKOUT_FIELD = (By.XPATH, "//input[@name=\"address[telephone]\"]")
    # Address field
    ADDRESS_CHECKOUT_FIELD = (By.XPATH, "//input[@name=\"address[address_1]\"]")
    # City field
    CITY_CHECKOUT_FIELD = (By.XPATH, "//input[@name=\"address[city]\"]")
    # Country field
    COUNTRY_CHECKOUT_FIELD = (By.XPATH, "//select[@name=\"address[country]\"]")
    # Province field
    PROVINCE_CHECKOUT_FIELD = (By.XPATH, "//select[@name=\"address[province]\"]")
    # Postal code field
    POSTAL_CODE_CHECKOUT_FIELD = (By.XPATH, "//input[@name=\"address[postcode]\"]")
    # Shipping method
    SHIPPING_METHOD_CHECKOUT_FIELD = (By.XPATH, "//input[@type=\"radio\"][@name=\"method\"]/ancestor::label//span["
                                                "@class=\"radio-unchecked\"]")
    # Payment method button
    PAYMENT_METHOD_CHECKOUT_BUTTON = (By.XPATH, "//div[@class=\"form-submit-button flex border-t border-divider mt-1 "
                                                "pt-1\"]//button")

    # Visa Mastercard Payment option
    VISA_MASTERCARD_PAYMENT_OPTION = (
        By.XPATH, "//div[@class=\"py-2\"]//*//img[@alt=\"Stripe\"]/parent::div/parent::div//a")

    # Stripe IFrame
    STRIPE_IFRAME = (By.XPATH, "//iframe[@title=\"Secure card payment input frame\"]")

    # Card number field
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@placeholder=\"Card number\"]")
    # Expiration date field
    EXPIRATION_DATE_FIELD = (By.XPATH, "//input[@placeholder=\"MM / YY\"]")
    # CVC field
    CVC_FIELD = (By.XPATH, "//input[@placeholder=\"CVC\"]")

    # Place Order button
    PLACE_ORDER_BUTTON = (By.XPATH, "//button//span[text()=\"Place Order\"]//parent::button")

    # Get information about the order
    # Contact information
    CONTACT_INFORMATION = (By.XPATH, "//div[text()=\"Contact information\"]/following-sibling::div")
    # Payment method
    PAYMENT_METHOD = (By.XPATH, "//div[text()=\"Payment Method\"]/following-sibling::div")
    # Shipping Address
    SHIPPING_ADDRESS = (By.XPATH, "//div[text()=\"Shipping Address\"]/following-sibling::div")
    # Billing Address
    BILLING_ADDRESS = (By.XPATH, "//div[text()=\"Billing Address\"]/following-sibling::div")
    # Items
    ITEMS = (By.XPATH, "//div[@id=\"summary-items\"]//tr")

    def __init__(self, browser):
        super().__init__(browser)
        self.address = None
        self.city = None
        self.postal_code = None
        self.telephone = None
        self.email = None
        self.full_name = None
        self.password = None

    def generate_customer_data(self):
        # Generate random email address and password
        self.full_name = generate_random_char_string(40)
        self.email = generate_random_mixed_string(10) + "@gmail.com"
        self.password = generate_random_mixed_string(10)

        self.telephone = generate_random_number_string(10)
        self.address = generate_random_char_string(30)
        self.city = generate_random_char_string(15)

        self.postal_code = generate_random_number_string(5)

    def open_home_page(self):
        self.browser.get("https://demo.evershop.io/")

    def click_sign_in_button(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def fill_full_name_field(self):
        self.enter_text(self.FULL_NAME_FIELD, self.full_name)

    def fill_email_field(self):
        self.enter_text(self.EMAIL_FIELD, self.email)

    def fill_password_field(self):
        self.enter_text(self.PASSWORD_FIELD, self.password)

    def click_sign_up_button(self):
        self.click(self.SIGN_UP_BUTTON)

    def random_navigation_bar(self):
        # Choose random navigation bar element
        self.click(random.choice(self.NAVIGATION_OPTIONS))

    def random_product(self):
        # Choose random product from the list
        self.click_random_element_from_list(self.PRODUCT_LIST)

    def add_product_to_cart(self):
        # Choose random product details
        for category in self.get_elements(self.PRODUCT_DETAILS):
            random.choice(category.find_elements(By.XPATH, ".//li")).click()

        # Add product to cart
        # Add a Sleep to make sure the product is added to the cart
        time.sleep(1)
        self.click(self.ADD_TO_CART_BUTTON)

    def click_cart_button(self):
        self.click(self.CART_BUTTON)

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_delivery_information_form(self):
        self.enter_text(self.FULL_NAME_CHECKOUT_FIELD, self.full_name)
        self.enter_text(self.TELEPHONE_CHECKOUT_FIELD, self.telephone)
        self.enter_text(self.ADDRESS_CHECKOUT_FIELD, self.address)
        self.enter_text(self.CITY_CHECKOUT_FIELD, self.city)
        self.click(self.COUNTRY_CHECKOUT_FIELD)
        self.select_dropdown_option(self.COUNTRY_CHECKOUT_FIELD, "United States")
        self.select_dropdown_option(self.PROVINCE_CHECKOUT_FIELD, "Ohio")
        self.enter_text(self.POSTAL_CODE_CHECKOUT_FIELD, self.postal_code)

        time.sleep(1)
        self.click(self.SHIPPING_METHOD_CHECKOUT_FIELD)

    def click_payment_method_button(self):
        self.click(self.PAYMENT_METHOD_CHECKOUT_BUTTON)

    def click_visa_mastercard_payment_option(self):
        self.click(self.VISA_MASTERCARD_PAYMENT_OPTION)

    def fill_payment_information(self):
        self.switch_to_iframe_by_xpath(self.STRIPE_IFRAME)

        self.enter_text(self.CARD_NUMBER_FIELD, "4242424242424242")
        self.enter_text(self.EXPIRATION_DATE_FIELD, "0424")
        self.enter_text(self.CVC_FIELD, "242")

        self.switch_to_main_content()

    def click_place_order_button(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def check_order_confirmation(self):
        output = ""
        output += "\nContact Information" + self.get_text(self.CONTACT_INFORMATION)
        output += "\nPayment Method" + self.get_text(self.PAYMENT_METHOD)
        output += "\nShipping Address" + self.get_text(self.SHIPPING_ADDRESS)
        output += "\nBilling Address" + self.get_text(self.BILLING_ADDRESS)
        output += "\nItems" + self.get_text(self.ITEMS)

        print(output)
