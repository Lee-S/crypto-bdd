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
load_dotenv()

scenarios('../features/private_api.feature')

API_URL = os.getenv("API_URL") + "/0/private/" # Environment variables are set in the .env file.
API_KEY = os.getenv("API_KEY")
API_SEC = os.getenv("API_SEC")
KEY_2FA = os.getenv("KEY_2FA")

def get_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def private_request(uri_path, data):
    headers = {}
    headers['API-Key'] = API_KEY
    headers['API-Sign'] = get_signature(uri_path, data, API_SEC)
    req = requests.post((API_URL + uri_path), headers=headers, data=data)
    json_data = req.json()
    return req


def get_otp():
    totp = pyotp.TOTP(KEY_2FA)
    return totp.now()


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
    response = private_request(API_URL + api,
        {
            "nonce": str(int(1000*time.time())),
            "otp": get_otp()
         })
    return response


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