Feature: Private API tests
  An registered user can connnect with signature and otp

#  Scenario: Retrieve user Balance
#    Given I am a registered user
#
#    When the "Balance" api is called
#
#    Then the response status is "200"
#    And the response json does not have errors
#    And a valid timestamp is returned
#    # Fictitious business requirement
#    And timestamp is within "2" seconds of current time


  Scenario: Retrieve user OpenOrders
    Given I am a registered user

    When the "OpenOrders" api is called

    Then the response status is "200"
    And the response json does not have errors
#    And a valid timestamp is returned
#    # Fictitious business requirement
#    And timestamp is within "2" seconds of current time
