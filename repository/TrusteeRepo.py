"""
    Requests trustee data
    Queries the JSON response and returns the results
"""
from collections import Counter
from connectors.TrusteeConnector import TrusteeConnector
TC = TrusteeConnector()


def test():
    n = 10
    global counted_tu
    top_users = {}
    for i in TC.all_trustees():
        for trustee in i:
            if trustee['trusteeType'] == 'user':
                common_name = trustee['data']['commonName']
                group_list_length = len(list(trustee['data']['memberOf']))
                is_active = str(trustee['data']['active'])
                top_users[common_name] = [group_list_length, is_active]
    counted_tu = Counter(top_users).most_common()[:n]
    print("Number of Trustees: ", len(counted_tu))
