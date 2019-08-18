"""Create report of the data"""
from os import getcwd, mkdir

import pandas as pd
import pandas_profiling as pf

# ======================================================================================================================
# Load data
# ======================================================================================================================
PROJECT_PATH = getcwd()
UFO_DATA = pd.read_csv('%s/data/complete.csv' % PROJECT_PATH, error_bad_lines=False)
# ======================================================================================================================
# Create report
# ======================================================================================================================
mkdir('%s/reports/' % PROJECT_PATH)
pf.ProfileReport(UFO_DATA).to_file('%s/reports/ProfileReport.html' % PROJECT_PATH)
