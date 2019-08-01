"""
    Connects to PSQL Classification table
    Queries the table and returns results
"""

class ClassificationRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table

    # Integer of the count of all the files in the Classification table
    def total_classifiable(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.table}""")
        return {'total_classifiable': self.cur.fetchall()[0][0]}

    # Integer of total documents classified ie those files that were assigned a categoryId
    def total_classified(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.table} WHERE "categoryId" != '-1'""")
        return {'total_classified': self.cur.fetchall()[0][0]}

    # Dictionary of categories and their counts
    def category_dict(self):
        self.cur.execute(f'''SELECT "categoryName", COUNT(*) FROM {self.table} GROUP BY "categoryName"''')
        return {'category_dict': dict(self.cur.fetchall())}

    # Dictionary of Business documents subcategories and numbers
    def busi_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
               "categoryName" = 'Business_Documents' GROUP BY  "subCategoryName"''')
        return {'busi_subcat_dict': dict(self.cur.fetchall())}

    # Dictionary of Financial documents subcategories and numbers
    def fina_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
                   "categoryName" = 'Financial_Documents' GROUP BY  "subCategoryName"''')
        return {'finan_subcat_dict': dict(self.cur.fetchall())}

    # Dictionary of Technical documents subcategories and numbers
    def tech_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
                   "categoryName" = 'Technical_Documents' GROUP BY  "subCategoryName"''')
        return {'tech_subcat_dict': dict(self.cur.fetchall())}

    # Dictionary of Legal documents subcategories and numbers
    def lega_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
                   "categoryName" = 'Legal_Documents' GROUP BY  "subCategoryName"''')
        return {'leg_subcat_dict': dict(self.cur.fetchall())}

    # Dictionary of Marketing documents subcategories and numbers
    def mark_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
                   "categoryName" = 'Marketing_Documents' GROUP BY  "subCategoryName"''')
        return {'mark_subcat_dict': dict(self.cur.fetchall())}

    # Dictionary of HR documents subcategories and numbers
    def hr_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.table} WHERE
                   "categoryName" = 'HR_Documents' GROUP BY  "subCategoryName"''')
        return {'hr_subcat_dict': dict(self.cur.fetchall())}

    # Total Sensitive documents
    def total_sensitive(self):
        self.cur.execute(f'''SELECT COUNT(*) FROM {self.table} WHERE "sensitive"''')
        return {'total_sensitive': self.cur.fetchall()[0][0]}

    # Dictionary of sensitive documents, their subcategories and counts
    def sens_subcat_dict(self):
        self.cur.execute(f"""select "subCategoryName", COUNT(*) from {self.table}
                            where "sensitive" = 't'
                            group by "subCategoryName" 
                            order by count(*) desc
                            limit 10;""")
        return {'sens_subcat_dict': dict(self.cur.fetchall())}

    # Total PII documents
    def total_pii(self):
        self.cur.execute(f'''SELECT COUNT(*) FROM {self.table} WHERE "containsPii"''')
        return {'total_pii': self.cur.fetchall()[0][0]}

    # Dictionary of PII documents subcategories and numbers
    def pii_subcat_dict(self):
        self.cur.execute(f'''SELECT "categoryName", COUNT(*) FROM {self.table} WHERE 
                    "containsPii" GROUP BY "categoryName"''')
        return {'pii_subcat_dict': dict(self.cur.fetchall())}

