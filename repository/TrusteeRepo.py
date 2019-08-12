"""
    Requests trustee data
    Queries the JSON response and returns the results
"""
from collections import Counter
from connectors.TrusteeConnector import TrusteeConnector
from collections import Counter
from datetime import datetime


class TrusteeRepo:
    def __init__(self):
        self.TC = TrusteeConnector()

    def users_number_of_groups(self):
        users_number_of_groups = {}
        for i in self.TC.all_trustees():
            for trustee in i:
                if trustee['trusteeType'] == 'user':
                    common_name = trustee['data']['commonName']
                    group_list_length = len(list(trustee['data']['memberOf']))
                    is_active = str(trustee['data']['active'])
                    users_number_of_groups[common_name] = [group_list_length, is_active]
        ordered_users_number_of_groups = Counter(users_number_of_groups).most_common()
        return ordered_users_number_of_groups

    def enabled_inactive_users(self):
        enabled_inactive_users = {}
        for i in self.TC.all_trustees():
            for t in i:
                try:
                    if t['data']['active'] == False:
                        if t['data']['disabled'] == False:
                            common_name = t['data']['commonName']

                            last_login = datetime.strptime(t['data']['lastLoginAt'], '%Y-%m-%dT%H:%M:%S.%fZ') \
                                .replace(microsecond=0)
                            enabled_inactive_users[common_name] = last_login
                except KeyError:
                    pass

        ordered_enabled_inactive_users = Counter(enabled_inactive_users).most_common()[::-1]
        return ordered_enabled_inactive_users

    def stale_password_active_users(self):
        stale_password_active_users = {}
        for i in self.TC.all_trustees():
            for trustee in i:
                if trustee['trusteeType'] == 'user':
                    if trustee['data']['active'] == True:
                        common_name = trustee['data']['commonName']
                        try:
                            pwd_last_change = datetime.strptime(trustee['data']['passwordLastChangedAt'],
                                                                '%Y-%m-%dT%H:%M:%S:%fZ').replace(microsecond=0)
                        except ValueError:
                            try:
                                pwd_last_change = datetime.strptime(trustee['data']['passwordLastChangedAt'],
                                                                    '%Y-%m-%dT%H:%M:%SZ').replace(microsecond=0)
                            except:
                                pwd_last_change = datetime.strptime(trustee['data']['passwordLastChangedAt'],
                                                                    '%Y-%m-%dT%H:%M:%S.%fZ').replace(microsecond=0)
                        if (datetime.now() - pwd_last_change).days >= 90:
                            last_login = datetime.strptime(trustee['data']['lastLoginAt'], '%Y-%m-%dT%H:%M:%S.%fZ') \
                                .replace(microsecond=0)
                            stale_password_active_users[common_name] = [pwd_last_change, last_login]
                        else:
                            pass
        ordered_stale_password_active_users = Counter(stale_password_active_users).most_common()[::-1]
        return ordered_stale_password_active_users

    def oldest_active_users(self):
        oldest_active_users = {}
        for i in self.TC.all_trustees():
            for trustee in i:
                if trustee['trusteeType'] == 'user':
                    if trustee['data']['active']:
                        common_name = trustee['data']['commonName']
                        created_at = datetime.strptime(trustee['data']['createdAt'], '%Y-%m-%dT%H:%M:%SZ[%Z]') \
                            .replace(microsecond=0)
                        last_login = datetime.strptime(trustee['data']['lastLoginAt'], '%Y-%m-%dT%H:%M:%S.%fZ') \
                            .replace(microsecond=0)
                        group_list_length = len(list(trustee['data']['memberOf']))
                        oldest_active_users[common_name] = [created_at, last_login, group_list_length]
        ordered_oldest_active_users = Counter(oldest_active_users).most_common()[::-1]
        return ordered_oldest_active_users
