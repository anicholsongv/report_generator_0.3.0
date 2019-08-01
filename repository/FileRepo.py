"""
    Connects to PSQL File table
    Queries the table and returns results
"""


class FileRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table
