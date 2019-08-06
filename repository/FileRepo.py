"""
    Connects to PSQL File file_table
    Queries the file_table and returns results
"""


class FileRepo:

    def __init__(self, cur, file_table):
        self.cur = cur
        self.file_table = file_table

    # Total discovered files
    def total_discovered(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.file_table}""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of all the files in the scanned share'}

    # Total discovered Bytes
    def total_discovered_bytes(self):
        self.cur.execute(f"""select SUM("contentLength") from {self.file_table}                   
                            ;""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Sum of all the file sizes discovered'}

    # Oldest files based on modification date
    def oldest_files(self):
        self.cur.execute(f"""select "lastModifiedAt", "createdAt", "path" from {self.file_table} 
                            where "createdAt" != '1970-01-01 01:00:00' 
                            and "fileType" != 'directory'
                            order by "lastModifiedAt" asc;""")
        return {'data': self.cur.fetchall(),
                'description': 'Oldest files by last modified, ignore 1970 date'}

    # Newest files based on modification date
    def newest_files(self):
        self.cur.execute(f"""select "lastModifiedAt", "createdAt", "path" from {self.file_table} 
                                    where "createdAt" != '1970-01-01 01:00:00'
                                    and "fileType" != 'directory' 
                                    order by "lastModifiedAt" desc;""")
        return {'data': self.cur.fetchall(),
                'description': 'Newest files by last modified'}

    # Newest folder based on modification date
    def newest_folders(self):
        self.cur.execute(f"""select "lastModifiedAt", "createdAt", "path" from {self.file_table} 
                                    where "createdAt" != '1970-01-01 01:00:00' 
                                    and "fileType" = 'directory'
                                    order by "lastModifiedAt" desc;""")
        return {'data': self.cur.fetchall(),
                'description': 'Newest folders by last modified'}

    # Oldest folder based on modification date
    def oldest_folders(self):
        self.cur.execute(f"""select "lastModifiedAt", "createdAt", "path" from {self.file_table} 
                                    where "createdAt" != '1970-01-01 01:00:00' 
                                    and "fileType" = 'directory'
                                    order by "lastModifiedAt" asc;""")
        return {'data': self.cur.fetchall(),
                'description': 'Newest folders by last modified'}
