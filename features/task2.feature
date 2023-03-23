# Created by jahirmedinacs at 22/03/2023

Feature: Testing API using Behave and Python

  Background:
    Given the endpoint "http://api.countrylayer.com/v2/alpha/{code}"
    And the API key "<your_api_key>"

  Scenario Outline: Get information for valid countries
    When I get information for "<code>"
    Then the response should have status code 200
    And the response should have the country name "<country_name>"

  Examples:
    | code | country_name                                         |
    | US   | United States of America                             |
    | DE   | Germany                                              |
    | GB   | United Kingdom of Great Britain and Northern Ireland |

  Scenario Outline: Get information for inexistent countries
    When I get information for "<code>"
    Then the response should have status code 404

  Examples:
    | code |
    | XX   |
    | YY   |

  Scenario: Validate new country addition using POST
    Given the endpoint "http://api.countrylayer.com/v2/all"
    And the API key "<your_api_key>"
    When I create a new country with name "Test Country", alpha2_code "TC" and alpha3_code "TCY"
    Then the response should have status code 500
