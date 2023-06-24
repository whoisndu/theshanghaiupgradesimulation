# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:39:55 2023

@author: NDU-PC
"""

import pandas as pd
# Read in the CSV file
csv_path = r"Price Points Filepath"
df = pd.read_csv(csv_path)
# Convert each column to a comma-separated value string
for column in df.columns:
csv_str = ','.join(str(value) for value in df[column])
print(f"{column}: {csv_str}")