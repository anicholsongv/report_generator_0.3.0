"""
    Connects to PSQL Classification classification_table
    Queries the classification_table and returns results
"""


class ClassificationRepo:

    def __init__(self, cur, classification_table):
        self.cur = cur
        self.classification_table = classification_table

    # Integer of the count of all the files in the Classification classification_table
    def total_classifiable(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.classification_table}""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of classifiable files'}

    # Integer of total documents classified ie those files that were assigned a categoryId
    def total_classified(self):
        self.cur.execute(f"""SELECT COUNT(*) FROM {self.classification_table} WHERE "categoryId" != '-1'""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of classifiable files'}

    # Dictionary of categories and their counts
    def category_dict(self):
        self.cur.execute(f'''SELECT "categoryName", COUNT(*) FROM {self.classification_table} GROUP BY "categoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Document Categories'}

    # Dictionary of Business documents subcategories and numbers
    def busi_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
               "categoryName" = 'Business_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Business Document Subcategories'}

    # Dictionary of Financial documents subcategories and numbers
    def fina_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
                   "categoryName" = 'Financial_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Financial Document Subcategories'}

    # Dictionary of Technical documents subcategories and numbers
    def tech_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
                   "categoryName" = 'Technical_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Technical Document Subcategories'}

    # Dictionary of Legal documents subcategories and numbers
    def lega_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
                   "categoryName" = 'Legal_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Legal Document Subcategories'}

    # Dictionary of Marketing documents subcategories and numbers
    def mark_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
                   "categoryName" = 'Marketing_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'Marketing Document Subcategories'}

    # Dictionary of HR documents subcategories and numbers
    def hr_subcat_dict(self):
        self.cur.execute(f'''SELECT "subCategoryName", COUNT(*) FROM {self.classification_table} WHERE
                   "categoryName" = 'HR_Documents' GROUP BY  "subCategoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'HR Document Subcategories'}

    # Total Sensitive documents
    def total_sensitive(self):
        self.cur.execute(f'''SELECT COUNT(*) FROM {self.classification_table} WHERE "sensitive"''')
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of sensitive files'}

    # Dictionary of sensitive documents, their subcategories and counts
    def sens_subcat_dict(self):
        self.cur.execute(f"""select "subCategoryName", COUNT(*) from {self.classification_table}
                            where "sensitive" = 't'
                            group by "subCategoryName" 
                            order by count(*) desc
                            limit 10;""")
        return {'data': dict(self.cur.fetchall()),
                'description': 'Sensitive Document Subcategories'}

    # Total PII documents
    def total_pii(self):
        self.cur.execute(f'''SELECT COUNT(*) FROM {self.classification_table} WHERE "containsPii"''')
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of Documents containing PII'}

    # Dictionary of PII documents categories and numbers
    def pii_cat_dict(self):
        self.cur.execute(f'''SELECT "categoryName", COUNT(*) FROM {self.classification_table} WHERE 
                    "containsPii" GROUP BY "categoryName"''')
        return {'data': dict(self.cur.fetchall()),
                'description': 'PII Documents Categories'}

    # Vectoriser model number
    def vectoriser_model_num(self):
        self.cur.execute(f'''select distinct "vectoriserModel" from {self.classification_table};''')
        return {'data': self.cur.fetchall()[0][0],
                'description': 'The model number of the vectoriser used'}

    # Classifier model number
    def classifier_model_num(self):
        self.cur.execute(f'''select distinct "classifierModel" from {self.classification_table};''')
        return {'data': self.cur.fetchall()[0][0],
                'description': 'The model number of the classifier used'}


