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

from repository.classification_repo import ClassificationRepo as CR
from rendering.ReportGraphs import PlotlyGraph
from rendering.HTMLRenderer import HTMLRenderer

import psycopg2
import json

with open('../config.json', 'r') as config_data:
    config_dict = json.load(config_data)


comp_name = config_dict["comp_name"]
#ip_add = scanned_host
scanned_share_name = config_dict["share_name"]

host = config_dict["pg_host"]
dbname = config_dict["pg_db"]
user = config_dict["pg_user"]
password = config_dict["pg_password"]
port = config_dict["pg_port"]
classification_table = config_dict["pg_classification_table"]
access_table = config_dict["pg_access_table"]
file_table = config_dict["pg_file_table"]
trustee_json_address = config_dict["trustee_json_address"]


conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password} port={port}")
cur = conn.cursor()

classification_repo = CR(cur, classification_table)
sensitive_data = classification_repo.sensitive_files()
renderer = PlotlyGraph(sensitive_data, "Sensitive Data Distribution", "")
sensitive_graph_file_name = renderer.horizontal_gv_bar()


main_html = HTMLRenderer(sensitive_data)
main_html.main_renderer()
