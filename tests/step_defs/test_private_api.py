import base64
import hashlib
import hmac
import os
import time
import urllib

import pyotp
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

#"/0/private/"


#TODO
@given("I am a registered user")
def any_user():
    """
    Dummy method for public API
    """
    pass


@when(parsers.parse('the "{api}" api is called'), target_fixture='api_response')
def api_response(api: str):
    """
    Using the API URL defined in .env file, call the passed in API method and return a response object
    """
    client = ApiClient(private_key=PVT_KEY, api_url=API_URL, key_2fa=KEY_2FA, api_key=API_KEY)
    req = client.private_request("/0/private/Balance", {})
    return req


@then("the response json does not have errors")
def response_json_has_no_errors(api_response):
    """
    Parse the json response and rerurn true if the errors list is empty.
    """
    assert len(api_response.json().get("error")) == 0


@then(parsers.parse('the response status is "{code:d}"'))
def response_code(api_response, code):
    """
    Assert the http status is as expeced.
    """
    assert api_response.status_code == code