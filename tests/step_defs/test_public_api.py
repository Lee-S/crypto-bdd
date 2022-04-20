import datetime
import os
import requests

from pytest_bdd import scenarios, given, when, then, parsers

from dotenv import load_dotenv
load_dotenv()

scenarios('../features/public_api.feature')

API_URL = os.getenv("API_URL") + "/0/public/"  # Environment variables are set in the .env file.


# TODO add type hints to show knowledge of strongly types language

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


@when(parsers.parse('the "{api}" api is called with params "{params}"'), target_fixture='api_response')
def api_with_params_response(api: str, params: str):
    """
    Using the API URL defined in .env file, call the passed in API method and return a response object
    """
    response = requests.get(f"{API_URL}{api}?{params}")
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


# TODO parameterize for response type
@then(parsers.parse('all expected AssetPair tags are present'))
def all_tags_present(api_response):
    """
    Check all expected tags are present on the response.  Libraries exist in Python to do this such
    as Pydantic, however I will manually verify a subset of response tags showing a range of tests
    """
    results = api_response.json()["result"]
    # Single result
    assert len(results) == 1  # Assuming only 1 pair was provided as parameters.
    # Correct asset
    assert "XXBTZUSD" in results.keys()
    asset = results["XXBTZUSD"]
    # Direct comparison
    assert asset["altname"] == "XBTUSD"
    assert asset["wsname"] == "XBT/USD"
    assert asset["aclass_base"] == "currency"
    assert asset["base"] == "XXBT"
    assert asset["aclass_quote"] == "currency"
    assert asset["quote"] == "ZUSD"
    assert asset["lot"] == "unit"
    # Test on iterable
    assert all(type(leverage) == int for leverage in asset["leverage_buy"])
    assert all(leverage > 0 for leverage in asset["leverage_sell"])
