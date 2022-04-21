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
