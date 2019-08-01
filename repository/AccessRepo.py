"""
    Connects to PSQL Access table
    Queries the table and returns results
"""


class AccessRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table
