"""
    Connects to PSQL File table
    Queries the table and returns results
"""


class FileRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table

    # Total discovered files
    def total_discovered(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.table}""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of all the files in the scanned share'

    # Total discovered Bytes
    def total_discovered_bytes(self):
        self.cur.execute(f"""select SUM("contentLength") from {self.table}                   
                            ;""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Sum of all the file sizes discovered'}

    def oldest_files_ten(self):
        self.cur.execute(f"""select "lastModifiedAt", "createdAt", "path" from {self.table} 
                            where "createdAt" != '1970-01-01 01:00:00' 
                            order by "lastModifiedAt" asc
                            limit 10;""")
        return {'data': dict(self.cur.fetchall()),
                'description': 'Oldest files by last modified, ignore 1970 date'}


