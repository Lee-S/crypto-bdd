Feature: Private API tests
  An registered user can connect with signature and otp


  Scenario: Retrieve user OpenOrders
    Given User credentials are set

    When the "OpenOrders" api is called

    Then the response status is "200"
    And the response json does not have errors
    And All mandatory attributes present on orders


