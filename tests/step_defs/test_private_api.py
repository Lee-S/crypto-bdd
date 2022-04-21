import os
import requests

from pytest_bdd import scenarios, given, when, then, parsers
from dotenv import load_dotenv
from crypto_client.client import ApiClient

load_dotenv()

scenarios('../features/private_api.feature')

API_URL = os.getenv("API_URL")  # Environment variables are set in the .env file.
API_KEY = os.getenv("API_KEY")
PVT_KEY = os.getenv("PVT_KEY")
KEY_2FA = os.getenv("KEY_2FA")


@given("User credentials are set")
def user_credentials_set():
    """
    Check necessary keys are available for authentication, variable is defined and not None/empty
    """
    assert all((API_URL, API_KEY, PVT_KEY, KEY_2FA))


@when(parsers.parse('the "{api}" api is called'), target_fixture='api_response')
def api_response(api: str):
    """
    Using the API URL defined in .env file, call the passed in API method and return a response object
    """
    client = ApiClient(private_key=PVT_KEY, api_url=API_URL, key_2fa=KEY_2FA, api_key=API_KEY)
    req = client.private_request(api, {})
    return req


@then("the response json does not have errors")
def response_json_has_no_errors(api_response: requests.Response):
    """
    Parse the json response and return true if the errors list is empty.
    """
    assert len(api_response.json().get("error")) == 0


@then(parsers.parse('the response status is "{code:d}"'))
def response_code(api_response: requests.Response, code: int):
    """
    Assert the http status is as expected.  (For the API in question also need to check the payload for error and result)
    """
    assert api_response.status_code == code

@then("All mandatory attributes present on orders")
def all_attributes_on_orders(api_response: requests.Response):
    """
    Define a set of expected attributes and check each order has these attributes.
    """
    data = api_response.json()
    for order in data["result"]["open"].values():
        all_attributes_present(order)


def all_attributes_present(order):
  MANDATORY_ATTRIBUTES = {
    "refid",
    "userref",
    "status",
    "opentm",
    "starttm",
    "expiretm",
    "descr",
    "vol",
    "vol_exec",
    "cost",
    "fee",
    "price",
    "stopprice",
    "limitprice",
    "misc",
    "oflags",
  }
  assert all(attribute in set(order.keys()) for attribute in MANDATORY_ATTRIBUTES)

  EXPECTED_ATTRIBUTES_DESCR = {
    "pair",
    "type",
    "ordertype",
    "price",
    "price2",
    "leverage",
    "order",
    "close",
  }
  assert all(attribute in set(order["descr"].keys()) for attribute in EXPECTED_ATTRIBUTES_DESCR)




