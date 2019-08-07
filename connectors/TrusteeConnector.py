"""
Connect to trustee json adn return ijson generator object
"""

import ijson
import requests
from ConfigReader import ConfigReader
CR = ConfigReader()


class TrusteeConnector:
    def __init__(self):
        self.trustee_json_address = CR.trustee_json_address
        self.trustee_json_username = CR.trustee_username
        self.trustee_json_password = CR.trustee_password
        self.json_connector()
        self.trustee_discoverer()

    def json_connector(self):
        auth_header = {
            'Accept': 'text/plain',
            'Content-Type': 'application/json',
            'cache-control': 'no-cache,no-cache',
        }

        auth_data = '{\n    "username": %s,\n    "password": %s \n}' \
                    % (self.trustee_json_username, self.trustee_json_password)

        token_response = requests.post(f'{self.trustee_json_address}/auth/token', headers=auth_header, data=auth_data)

        token = token_response.text

        self.secure_header = {
            'Authorization': f'Bearer {token}',
            'cache-control': 'no-cache,no-cache',
        }
        print("Connection Establised")

    def trustee_discoverer(self):
        requests.get(f'{self.trustee_json_address}/discovery/trustees', headers=self.secure_header)
        print("Discover Trustees")

    def all_trustees(self):
        all_trustees_response = requests.get(f'{self.trustee_json_address}/trustee/all',
                                             headers=self.secure_header)
        print("All trustees")
        return ijson.items(all_trustees_response.text, '')


