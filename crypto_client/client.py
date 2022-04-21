import base64
import hashlib
import hmac
import time
import urllib
from typing import Dict

import pyotp
import requests


class ApiClient:

    def __init__(self, private_key:str, api_url:str, key_2fa:str, api_key:str):
        self.private_key = private_key
        self.api_url = api_url
        self.key_2fa = key_2fa
        self.api_key = api_key


    def get_api_sign(self, urlpath, data):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()
        mac = hmac.new(base64.b64decode(self.private_key), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()


    def private_request(self, uri_path:str, data: Dict):
        headers = {}
        data["nonce"] = self.get_nonce()
        data["otp"] = self.get_otp(self.key_2fa)
        headers['API-Key'] = self.api_key
        headers['API-Sign'] = self.get_api_sign(uri_path, data)
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        req = requests.post((self.api_url + uri_path), headers=headers, data=data)
        return req


    @staticmethod
    def get_otp(key_2fa):
        totp = pyotp.TOTP(key_2fa)
        return totp.now()

    @staticmethod
    def get_nonce():
        return str(int(1000*time.time()))