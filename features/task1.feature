# Created by jahirmedinacs at 22/03/2023
Feature: Sign in and checkout

  Background: Generate customer data
    Given a generated customer with all customer data

  Scenario: Sign in, add products to cart, and checkout
    Given the user opens the Home page
    When the user clicks the "Sign in" button
    And the user fills the "Email address" and "Password" fields
    And the user clicks the "Create an account" button
    And the user logs in
    And the user selects 3 different products and adds them to the cart with different quantities
    And the user goes to the Checkout page and clicks on "Checkout"
    And the user fills the shipping address and submits
    And the user clicks on "success" to get correct card information
    And the user fills the payment information
    And the user clicks "Place Order"
    Then the order is created successfully with the correct information for Contact, Payment, Shipping Address, Billing Address, and Items
