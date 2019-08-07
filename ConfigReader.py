"""
Reads the config json and returns the entries through its methods
These entries are used throughout the classes of the report generator
"""


import psycopg2
import json

with open('../config.json', 'r') as config_data:
    config_dict = json.load(config_data)


class ConfigReader:
    # Initialise with config data
    def __init__(self):
        self.config_dict = config_dict
        self.host = config_dict["pg_host"]
        self.dbname = config_dict["pg_db"]
        self.user = config_dict["pg_user"]
        self.password = config_dict["pg_password"]
        self.port = config_dict["pg_port"]
        self.comp_name = config_dict["comp_name"]
        self.scanned_share_name = config_dict["share_name"]
        self.classification_table = config_dict["pg_classification_table"]
        self.access_table = config_dict["pg_access_table"]
        self.file_table = config_dict["pg_file_table"]
        self.trustee_json_address = config_dict["trustee_json_address"]
        self.trustee_username = config_dict["trustee_username"]
        self.trustee_password = config_dict["trustee_password"]

    # Postgres (psycopg2) Entries
    def host(self):
        return self.host

    def dbname(self):
        return self.dbname

    def user(self):
        return self.user

    def password(self):
        return self.password

    def port(self):
        return self.port

    def classification_table(self):
        return self.classification_table

    def access_table(self):
        return self.access_table

    def file_table(self):
        return self.file_table

    # JSON Entries
    def trustee_json_address(self):
        return self.trustee_json_address

    def trustee_username(self):
        return self.trustee_username

    def trustee_password(self):
        return self.trustee_password

    # Universal Entries
    def comp_name(self):
        return self.comp_name

    def scanned_share_name(self):
        return self.scanned_share_name










