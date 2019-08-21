"""Investigate which are the most visited cities and how the shape of the UFO is related to its duration."""
from os import getcwd

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# ======================================================================================================================
# Load data
# ======================================================================================================================
PROJECT_PATH = getcwd()
UFO_DATA = pd.read_csv('%s/data/scrubbed.csv' % PROJECT_PATH, low_memory=False)
# ======================================================================================================================
# Top 10 cities
# ======================================================================================================================
UFO_DATA.groupby('city').count().datetime.sort_values().tail(10)
ax = plt.figure(figsize=(10, 8)).add_subplot(111)
UFO_DATA.groupby('city').count().datetime.sort_values().tail(10).plot.bar(ax=ax)
plt.show()
# ======================================================================================================================
# Visualize ufo shapes
# ======================================================================================================================
UFO_DATA['duration (seconds)'] = UFO_DATA['duration (seconds)'].str.replace('`', '').astype('float')
ax = plt.figure(figsize=(10, 8)).add_subplot(111)
sns.boxplot(x='shape', y='duration (seconds)', data=UFO_DATA, ax=ax)
plt.title('Duration vs Shape boxplot')
plt.ylim(0, 2000)
plt.tick_params('x', rotation=90, labelsize=20)
plt.show()
