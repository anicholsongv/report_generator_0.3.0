class ClassificationRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table

    def sensitive_files(self):
        self.cur.execute(f"""select "subCategoryName", count(*) from {self.table}
                            where "sensitive" = 't'
                            group by "subCategoryName" 
                            order by count(*) desc
                            limit 10;""")
        return {'graph_data': dict(self.cur.fetchall())}
