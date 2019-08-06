"""
Queries that join the Classification and File psql tables

"""
from collections import OrderedDict
from repository.DataSorter import DataSorter

class ClassificationFileRepo:

    def __init__(self, cur, file_table, classification_table, scanned_share_name):
        self.cur = cur
        self.file_table = file_table
        self.classification_table = classification_table
        self.scanned_share_name = scanned_share_name





    # Total classified Bytes
    def total_classified_bytes(self):
        self.cur.execute(f"""select SUM(fi."contentLength") from {self.file_table} as fi
                        join {self.classification_table} as cl
                        on fi."id" = cl."id"
                        ;""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Sum of all the file sizes classified'}

    # File types count and their average sizes
    '''def 
        self.cur.execute(f"""select fi."fileType", count(fi."fileType"),
                              ROUND(AVG(fi."contentLength"), 5)
                              from {self.file_table} as fi join {self.classification_table} as cl
                              on fi."id" = cl."id"
                              group by fi."fileType"
                          order by COUNT(fi."fileType") desc;""")
        ftcavg_dict = self.cur.fetchall()'''

    # Total images count
    def total_images(self):
        self.cur.execute(f"""select count(*) from {self.classification_table} as cl
                       join {self.file_table} as fi
                       on fi."id" = cl."id"
                       and (LOWER(fi."fileType") = 'bmp'
                       or LOWER(fi."fileType") = 'png'
                       or LOWER(fi."fileType") = 'svg'
                       or LOWER(fi."fileType") = 'png'
                       or LOWER(fi."fileType") = 'gif'
                       or LOWER(fi."fileType") = 'tiff'
                       or LOWER(fi."fileType") = 'jpg'
                       or LOWER(fi."fileType") = 'jpeg')
                       ;""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Count of all image file extensions in classified'}

    # Images in folders
    def total_images_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and (LOWER(fi."fileType") = 'bmp'
                           or LOWER(fi."fileType") = 'png'
                           or LOWER(fi."fileType") = 'svg'
                           or LOWER(fi."fileType") = 'png'
                           or LOWER(fi."fileType") = 'gif'
                           or LOWER(fi."fileType") = 'tiff'
                           or LOWER(fi."fileType") = 'jpg'
                           or LOWER(fi."fileType") = 'jpeg')
                            group by fi."path" 
                            order by count(*) desc
                           ;""")

        image_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v) for (k, v) in
                               self.cur.fetchall()]
        image_folder_dict = {}
        for k, v in image_folder_tuples:
            if k not in image_folder_dict.keys():
                image_folder_dict[k] = v
            else:
                image_folder_dict[k] += v

        image_folder_dict = OrderedDict(reversed(sorted(image_folder_dict.items(), key=lambda i: i[1])))
        return {'data': image_folder_dict,
                'description': 'The paths of folders that contain images with the amount in each'}

    # The number of copied files
    def total_copied_files(self):
        self.cur.execute(f"""select count(*) from {self.file_table} as fi 
                            join {self.classification_table} as cl
                            on fi."id" = cl."id"
                            and "lastModifiedAt" < "createdAt"
                            and "sensitive" = 'True'""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Total number of copied classified files'}

    # PII files that were copied
    def total_pii_copied_files(self):
        self.cur.execute(f"""select count(*) from file as fi
                            join classification as cl
                            on fi."id" = cl."id"
                            and fi."createdAt" > fi."lastModifiedAt"
                            and cl."containsPii" = 't'""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Total number of copied PII files'}

    # Business documents in folders
    def business_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'Business_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        business_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                                  for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        business_folder_dict = {}
        for k, v in business_folder_tuples:
            if k not in business_folder_dict.keys():
                business_folder_dict[k] = v
            else:
                business_folder_dict[k] += v
        # Create Ordered Dictionary
        business_folder_dict = OrderedDict(reversed(sorted(business_folder_dict.items(), key=lambda i: i[1])))
        return {'data': business_folder_dict,
                'description': 'Folders with the most Business documents'}

    # Finance documents in folders
    def finance_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'Financial_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        finance_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                                 for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        finance_folder_dict = {}
        for k, v in finance_folder_tuples:
            if k not in finance_folder_dict.keys():
                finance_folder_dict[k] = v
            else:
                finance_folder_dict[k] += v
        # Create Ordered Dictionary
        finance_folder_dict = OrderedDict(reversed(sorted(finance_folder_dict.items(), key=lambda i: i[1])))
        return {'data': finance_folder_dict,
                'description': 'Folders with the most Financial documents'}

    # Technical documents in folders
    def technical_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'Technical_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        technical_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                                   for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        technical_folder_dict = {}
        for k, v in technical_folder_tuples:
            if k not in technical_folder_dict.keys():
                technical_folder_dict[k] = v
            else:
                technical_folder_dict[k] += v
        # Create Ordered Dictionary
        technical_folder_dict = OrderedDict(reversed(sorted(technical_folder_dict.items(), key=lambda i: i[1])))
        return {'data': technical_folder_dict,
                'description': 'Folders with the most Technical documents'}

    # Legal documents in folders
    def legal_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'Legal_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        legal_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                               for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        legal_folder_dict = {}
        for k, v in legal_folder_tuples:
            if k not in legal_folder_dict.keys():
                legal_folder_dict[k] = v
            else:
                legal_folder_dict[k] += v
        # Create Ordered Dictionary
        legal_folder_dict = OrderedDict(reversed(sorted(legal_folder_dict.items(), key=lambda i: i[1])))
        return {'data': legal_folder_dict,
                'description': 'Folders with the most Legal documents'}

    # Marketing documents in folders
    def marketing_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'Marketing_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        marketing_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                                   for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        marketing_folder_dict = {}
        for k, v in marketing_folder_tuples:
            if k not in marketing_folder_dict.keys():
                marketing_folder_dict[k] = v
            else:
                marketing_folder_dict[k] += v
        # Create Ordered Dictionary
        marketing_folder_dict = OrderedDict(reversed(sorted(marketing_folder_dict.items(), key=lambda i: i[1])))
        return {'data': marketing_folder_dict,
                'description': 'Folders with the most Marketing documents'}

    # HR documents in folders
    def hr_category_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and cl."categoryName" = 'HR_Documents'
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        hr_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                            for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        hr_folder_dict = {}
        for k, v in hr_folder_tuples:
            if k not in hr_folder_dict.keys():
                hr_folder_dict[k] = v
            else:
                hr_folder_dict[k] += v
        # Create Ordered Dictionary
        hr_folder_dict = OrderedDict(reversed(sorted(hr_folder_dict.items(), key=lambda i: i[1])))
        return {'data': hr_folder_dict,
                'description': 'Folders with the most HR documents'}

    # PII in folders
    def pii_folders(self):
        self.cur.execute(f"""select fi."path", count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and "containsPii"
                           group by fi."path" 
                           order by count(*) desc;""")
        # Get folder path, exclude share name
        pii_folder_tuples = [(k.rsplit('/', 1)[0].split(f'{self.scanned_share_name}', 1)[-1], v)
                             for (k, v) in self.cur.fetchall()]
        # Count and sort documents in to folders
        pii_folder_dict = {}
        for k, v in pii_folder_tuples:
            if k not in pii_folder_dict.keys():
                pii_folder_dict[k] = v
            else:
                pii_folder_dict[k] += v
        # Create Ordered Dictionary
        pii_folder_dict = OrderedDict(reversed(sorted(pii_folder_dict.items(), key=lambda i: i[1])))
        return {'data': pii_folder_dict,
                'description': 'Folders with the most PII documents'}

    # PII among file types
    def pii_filetypes(self):
        self.cur.execute(f"""select LOWER(fi."fileType"), count(*) from {self.classification_table} as cl
                           join {self.file_table} as fi
                           on fi."id" = cl."id"
                           and "containsPii"
                            and fi."fileType" != 'directory'
                           group by LOWER(fi."fileType")
                           order by count(*) desc;""")
        return {'data': dict(self.cur.fetchall()),
                'description': 'File types containing PII'}

    # Image Category distribution
    def image_categories(self):
        self.cur.execute(f"""select cl."categoryName", count(*) from {self.classification_table} as cl
                            join {self.file_table} as fi
                            on fi."id" = cl."id"
                            and (LOWER(fi."fileType") = 'bmp'
                           or LOWER(fi."fileType") = 'png'
                           or LOWER(fi."fileType") = 'svg'
                           or LOWER(fi."fileType") = 'png'
                           or LOWER(fi."fileType") = 'gif'
                           or LOWER(fi."fileType") = 'tiff'
                           or LOWER(fi."fileType") = 'jpg'
                           or LOWER(fi."fileType") = 'jpeg')
                           group by cl."categoryName";""")
        return {'data': dict(self.cur.fetchall()),
                'description': 'Image Distribution among Categories'}

    # Copied files containing PII
    def total_copied_pii(self):
        self.cur.execute(f"""select count(*) from {self.file_table} as fi
                            join {self.classification_table} as cl
                            on fi."id" = cl."id"
                            and fi."createdAt" > fi."lastModifiedAt"
                            and cl."containsPii" = 't'""")
        return {'data': self.cur.fetchall()[0][0],
                'description': 'Total number of copied files'}

    # Categories of copied files
    def copied_categories(self):
        self.cur.execute(f"""select cl."categoryName", count(*) from {self.file_table} as fi
                            join {self.classification_table} as cl
                            on fi."id" = cl."id"
                            and fi."createdAt" > fi."lastModifiedAt"
                            group by cl."categoryName";""")
        return {'data': dict(self.cur.fetchall()),
                'description': 'Categories of Copied Files'}
