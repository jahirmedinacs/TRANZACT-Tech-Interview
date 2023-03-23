from behave import *
from pages.task1_page import Task1Page

use_step_matcher("re")


@given("a generated customer with all customer data")
def a_generated_customer_with_all_customer_data(context):
    context.task1_page = Task1Page(context.browser)

    # generate customer data (Email address and Password) by a random string
    context.task1_page.generate_customer_data()


@given("the user opens the Home page")
def the_user_opens_the_home_page(context):
    context.task1_page.open_home_page()


@when('the user clicks the "Sign in" button')
def the_user_clicks_the_sign_in_button(context):
    context.task1_page.click_sign_in_button()
    context.task1_page.click_create_account_button()


@step('the user fills the "Email address" and "Password" fields')
def the_user_fills_the_email_address_and_password_fields(context):
    context.task1_page.fill_full_name_field()
    context.task1_page.fill_email_field()
    context.task1_page.fill_password_field()


@step('the user clicks the "Create an account" button')
def step_impl(context):
    context.task1_page.click_sign_up_button()


@step("the user logs in")
def the_user_logs_in(context):
    pass


@step("the user selects 3 different products and adds them to the cart with different quantities")
def the_user_selects_3_different_products_and_adds_them_to_the_cart_with_different_quantities(context):
    for ii in range(3):
        context.task1_page.random_navigation_bar()
        context.task1_page.random_product()
        context.task1_page.add_product_to_cart()


@step('the user goes to the Checkout page and clicks on "Checkout"')
def the_user_goes_to_the_checkout_page_and_clicks_on_checkout(context):
    context.task1_page.click_cart_button()
    context.task1_page.click_checkout_button()


@step("the user fills the shipping address and submits")
def the_user_fills_the_shipping_address_and_submits(context):
    context.task1_page.fill_checkout_delivery_information_form()


@step('the user clicks on "success" to get correct card information')
def the_user_clicks_on_success_to_get_correct_card_information(context):
    context.task1_page.click_payment_method_button()
    context.task1_page.click_visa_mastercard_payment_option()


@step("the user fills the payment information")
def the_user_fills_the_payment_information(context):
    context.task1_page.fill_payment_information()


@step('the user clicks "Place Order"')
def the_user_clicks_place_order(context):
    context.task1_page.click_place_order_button()


@then(
    "the order is created successfully with the correct information for Contact, Payment, Shipping Address, Billing Address, and Items")
def the_order_is_created_successfully_with_the_correct_information_for_contact_payment_shipping_address_billing_address_and_items(
        context):
    context.task1_page.check_order_confirmation()
