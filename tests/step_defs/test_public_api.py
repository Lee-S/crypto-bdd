import datetime
import os

import requests

from pytest_bdd import scenarios, given, when, then, parsers

from dotenv import load_dotenv

load_dotenv()

scenarios('../features/public_api.feature')

API_URL = os.getenv("API_URL")      # Environment variables are set in the .env file.


@given("I am any user")
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
    response = requests.get(API_URL + api)
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


@then("a valid timestamp is returned", target_fixture="timestamp")
def timestamp_valid(api_response):
    """
    Check that unixtime is included in the response object and that it can be parsed into a datetime
    Return the datetime object for further processing.
    """
    assert "unixtime" in api_response.json()["result"]
    epoc_time = api_response.json()["result"]["unixtime"]
    timestamp = datetime.datetime.fromtimestamp(epoc_time)
    return timestamp


@then(parsers.parse('timestamp is within "{tolerance_secs:d}" seconds of current time'))
def timstamp_within_tolerance(timestamp, tolerance_secs):
    """
    A fictitious business requirement as an example.  Check the timestamp from the server is "within sensible range"
    """
    t_delta = datetime.datetime.now() - timestamp
    assert t_delta < datetime.timedelta(seconds=tolerance_secs)