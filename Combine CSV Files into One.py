# -*- coding: utf-8 -*-
""" 
Created on Sat Jun 24 16:32:12 2023

@author: NDU-PC
"""

# List of files to load
file_list = ["Ankr Amount Deposit Count filepath",
"Stakewise Amount Deposit Count filepath",
"Cream Finance Amount Deposit Count filepath",
"Lido Finance Amount Deposit Count filepath",
"Frax Finance Amount Deposit Count filepath"]
# Create an empty dictionary to hold the dataframes
df_dict = {}
# Load each file into a dataframe and add it to the dictionary
for file in file_list:
df = pd.read_csv(file)
df_dict[file] = df
# Merge all dataframes on the "Deposit" column
df_merged = pd.concat(df_dict.values()).groupby("Deposit",
as_index=False).sum()
# Save the result to a .csv file
df_merged.to_csv("All Liquid Stakers", index=False)
# Print the "Deposit" and "Count" columns
for index, row in df_merged.iterrows():
deposit = row["Deposit"]
count = row["Count"]
print(f"Deposit - {deposit}: Count - {count}")