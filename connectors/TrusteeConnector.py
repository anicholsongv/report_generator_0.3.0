"""
Connect to trustee json adn return ijson generator object
"""

import ijson.backends.yajl2_cffi as ijson
import requests
from ConfigReader import ConfigReader
from collections import Counter
from urllib.request import urlopen, Request


class TrusteeConnector:
    def __init__(self):
        self.CR = ConfigReader()
        self.trustee_json_address = self.CR.trustee_json_address
        self.trustee_json_username = self.CR.trustee_username
        self.trustee_json_password = self.CR.trustee_password
        # self.json_connector()
        self.trustee_discoverer()

    def get_token(self):
        auth_header = {
            'Accept': 'text/plain',
            'Content-Type': 'application/json',
            'cache-control': 'no-cache,no-cache',
        }

        auth_data = '{\n    "username": %s,\n    "password": %s \n}' \
                    % (self.trustee_json_username, self.trustee_json_password)

        token_response = requests.post(f'{self.trustee_json_address}/auth/token', headers=auth_header, data=auth_data)

        token = token_response.text

        # self.secure_header = {
        #     'Authorization': f'Bearer {token}',
        #     'cache-control': 'no-cache,no-cache',
        # }

        print("Connection Establised")
        return token

    def trustee_discoverer(self):
        requests.get(f'{self.trustee_json_address}/discovery/trustees', headers={
            'Authorization': f'Bearer {self.get_token}', 'cache-control': 'no-cache,no-cache'})
        print("Discover Trustees")

    def all_trustees(self):
        # all_trustees_response = requests.get(f'{self.trustee_json_address}/trustee/all',
        #                                      headers=self.secure_header)
        print("All Trustees")

        # print(all_trustees_response)
        print('----------')
        req = Request(f'{self.trustee_json_address}/trustee/all')
        req.add_header('Authorization', f'Bearer {self.get_token}')
        req.add_header('cache-control', 'no-cache,no-cache')
        f = urlopen(req)

        return ijson.items(f, '')

    def trustee_aggregates(self):
        respnse = requests.get(f'{self.trustee_json_address}/reporting/powerful-users', headers={
            'Authorization': f'Bearer {self.get_token}', 'cache-control': 'no-cache,no-cache'}).text

        return respnse
