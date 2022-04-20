Feature: Public API tests
  Any user can retrieve information from the public API.

  Scenario: Retrieve exchange server time
    Given I am any user

    When the "Time" api is called

    Then the response status is "200"
    And the response json does not have errors
    And a valid timestamp is returned
    # Fictitious business requirement
    And timestamp is within "2" seconds of current time



  Scenario: Retrieve asset pair from exchange
    Given I am any user

    When the "AssetPairs" api is called with params "pair=XXBTZUSD"

    Then the response status is "200"
    And the response json does not have errors
    And all expected AssetPair tags are present