import psycopg2
import jinja2
from weasyprint import HTML, CSS
import plotly.graph_objs as go
import plotly.io as pio
import collections
from collections import Counter
from collections import OrderedDict
import json
from datetime import datetime
import requests
import math

import ijson

from repository.ClassificationRepo import ClassificationRepo
from rendering.HorizGraphDrawer import HorizGraphDrawer
from rendering.HtmlBodyRenderer import HtmlBodyRenderer
from rendering.PdfRenderer import PdfRenderer
from repository.ClassificationFileRepo import ClassificationFileRepo
from repository.FileRepo import FileRepo
from ConfigReader import ConfigReader

import psycopg2


CR = ConfigReader()

conn = psycopg2.connect(f"host={CR.host} dbname={CR.dbname} user={CR.user} password={CR.password} port={CR.port}")
cur = conn.cursor()

# cr = ClassificationRepo(cur, classification_table)
#
# sensitive_data = cr.sens_subcat_dict()
#
# renderer = HorizGraphDrawer(sensitive_data['data'], sensitive_data['description'], "")
#
# sensitive_data.update(renderer.horizontal_gv_bar())
#
#
# main_html = HtmlBodyRenderer(sensitive_data)
# main_html_path = main_html.main_renderer()
# full_html_list = []
# full_html_list.append(main_html_path)
# hbr = PdfRenderer(full_html_list)
# hbr.pdf_writer()
test = ClassificationFileRepo(cur, CR.file_table, CR.classification_table, CR.scanned_share_name)
test2 = FileRepo(cur, CR.file_table)

print(CR.host, CR.dbname)
print(test.legal_category_folders())
print(test2.oldest_folders())
