# crypto-bdd
### An exercise in testing APIs using BDD.

A crypto client was developed to be used by the BDD features.  Some pyest unittests exist for a few parts of this.
pytest-tdd library was used to write BDD feature files for public and private API tests, along with thier step implementation.


1. Checkout repo
`git clone https://github.com/Lee-S/crypto-bdd.git`

2. Create a .env file in the root of the project.  This contains secrets that are not committed to github
```
API_URL="https://api.EXCHANGE.com/"
API_KEY="XYZ123ABC"
PVT_KEY="XYZ123ABC"
KEY_2FA="ABCABC"
```

3. Build the Docker image
`docker build -t bdd_image .`

4. Run the container.  Where 80 is an unused port on your machine
```
docker run --rm -it --name bdd_instance -p 80:7000 localhost/bdd_image
```

5. Navigate to the url http://127.0.0.1/  where you will see an html, and junit xml report of test results.
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

