# crypto-bdd
### An exercise in testing APIs using BDD.



The pytest-tdd library was used to write BDD feature files for both public and private API tests, found in tests/features.  The implementation steps can be found in tests/steps_defs.  A reusable crypto client was developed and is called by the BDD Featrure tests.  A few unit tests for the client are in  unittests.

I have attempetd to demo a few different examples of test techniques, yet the test suite is not exchaustive.

## To run the tests from the Docker image

1. Checkout repo
```
git clone https://github.com/Lee-S/crypto-bdd.git && crypto_bdd
```

2. Create a .env file in the root of the project.  This contains secrets that are not committed to github
```
API_URL="https://api.EXCHANGE.com"
API_KEY="<YOUR ACCOUNT API KEY>"
PVT_KEY="<YOUR PRIVATE KEY>"
KEY_2FA="<YOUR 2FA SETUP KEY>"
```

3. Build the Docker image
```
docker build -t bdd_image .
```

4. Run the container.  Where 80 is an unused port on your machine
```
docker run --rm -it --name bdd_instance -p 80:7000 bdd_image
```

You will see the tests run.

```
collected 5 items                                                                                                                                  

tests/step_defs/test_private_api.py::test_retrieve_user_openorders 
Feature: Private API tests
    Scenario: Retrieve user OpenOrders PASSED

tests/step_defs/test_public_api.py::test_retrieve_exchange_server_time 
Feature: Public API tests
    Scenario: Retrieve exchange server time PASSED

tests/step_defs/test_public_api.py::test_retrieve_asset_pair_from_exchange 
Feature: Public API tests
    Scenario: Retrieve asset pair from exchange PASSED

tests/unittest/test_client.py::test_get_api_sign_returns_expected_signature PASSED                                                           [ 20%]
tests/unittest/test_client.py::test_private_request_open_orders_returns_no_errors_and_empty_orders PASSED                                    [ 40%]

---------------------------------------------- generated xml file: /app/reports/crypto_bdd_junit.xml -----------------------------------------------
--------------------------------------------- generated html file: file:///app/reports/crypto_bdd.html ---------------------------------------------
================================================================ 5 passed in 1.30s =================================================================
Serving HTTP on 0.0.0.0 port 7000 (http://0.0.0.0:7000/) ...
```

5. Navigate to the url http://127.0.0.1/  (if running localy, or use remote server) where you will see an html, and junit xml report of test results.


