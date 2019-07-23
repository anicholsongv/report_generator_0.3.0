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
from ReportGraphs import PlotlyGraph
import ijson