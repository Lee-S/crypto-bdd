import os

from dotenv import load_dotenv
load_dotenv()

from crypto_client.client import ApiClient

API_URL = os.getenv("API_URL")  # Environment variables are set in the .env file.
API_KEY = os.getenv("API_KEY")
PVT_KEY = os.getenv("PVT_KEY")
KEY_2FA = os.getenv("KEY_2FA")

def test_get_api_sign_returns_expected_signature():
    data = {
        "nonce": "1616492376594",
        "ordertype": "limit",
        "pair": "XBTUSD",
        "price": 37500,
        "type": "buy",
        "volume": 1.25
    }
    private_key = "kQH5HW/8p1uGOVjbgWA7FunAmGO8lsSUXNsu3eow76sz84Q18fWxnyRzBHCd3pd5nE9qa99HAZtuZuj6F1huXg=="
    uri_path = "/0/private/AddOrder"
    expected_api_sign = "4/dpxb3iT4tp/ZCVEwSnEsLxx0bqyhLpdfOpc6fn7OR8+UClSV5n9E6aSS8MPtnRfp32bAb0nmbRn6H8ndwLUQ=="

    client = ApiClient(private_key=private_key,
                       api_url='',
                       key_2fa='',
                       api_key='',)
    assert client.get_api_sign(uri_path, data) == expected_api_sign


def test_private_request_header_calls_requests_post_with_correct_headers():
    client = ApiClient(private_key=PVT_KEY,
                       api_url=API_URL,
                       key_2fa=KEY_2FA,
                       api_key=API_KEY)

    req = client.private_request("/0/private/OpenOrders", {})
    assert req
    payload = req.json()
    assert payload

