"""
Queries that join the Classification and File psql tables

"""


class ClassificationFileRepo:

    def __init__(self, cur, table):
        self.cur = cur
        self.table = table


# Top 10 subcat confidence

    cur.execute(f"""select cl."path", fi."fileType", cl."categoryName",
                    cl."subCategoryName", cl."containsPii", cl."sensitive",    
                    cl."subCategoryConfidence"
                    from {file_table} as fi
                    join {classification_table} as cl
                    on fi."id" = cl."id"
                    order by cl."subCategoryConfidence" desc
                    limit 10
                    ;""")


    # Classified Bytes

    cur.execute(f"""select SUM(fi."contentLength") from {file_table} as fi
                    join {classification_table} as cl
                    on fi."id" = cl."id"
                    ;""")
    class_bytes_total = cur.fetchall()[0][0]

    # File types count and their average sizes
    cur.execute(f"""select fi."fileType", count(fi."fileType"),
                          ROUND(AVG(fi."contentLength"), 5)
                          from {file_table} as fi join {classification_table} as cl
                          on fi."id" = cl."id"
                          group by fi."fileType"
                      order by COUNT(fi."fileType") desc;""")
    ftcavg_dict = cur.fetchall()

    # Total images count

    cur.execute(f"""select count(*) from {classification_table} as cl
                   join {file_table} as fi
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

    image_count = cur.fetchall()[0][0]

    # Images in folders
    cur.execute(f"""select fi."path", count(*) from {classification_table} as cl
                       join {file_table} as fi
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
