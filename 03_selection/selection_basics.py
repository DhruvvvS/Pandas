# IMPORTING SECTION IS IN THE DATASET FOLDER

# Pandas Selection Basics

# Selection = The process of selecting specific rows and columns from a pandas DataFrame for analysis and manipulation.
#             Pandas provides several methods for selecting data, including .loc, .iloc, and boolean indexing.

import pandas as pd

df = pd.read_csv("F:/Git/Pandas/Datasets/data.csv")  # Importing a CSV file into a DataFrame

# Selection By Columns
print(df["Name"])  # Selecting a single column by label
print(df["Name"].to_string())  # Displaying the selected column as a string representation
print(df[["Name", "Height"]])  # Selecting multiple columns by label
print(df[["Name", "Height"]].to_string()) 

# Selection By Rows
print(df.loc[0])  # Selecting a single row by label (index)

# We can also pass Name as the index to select a row by label of name rather than the index number.
df_indexed = df.set_index("Name")
print(df_indexed.loc["Pikachu"])  # Selecting a row by label (index) after setting 'Name' as the index

print(df_indexed.loc["Charizard", ["Height", "Weight"]])  # Selecting a specific column for a row by label (index) after setting 'Name' as the index

# Selecting multiple rows and columns by label (index) after setting 'Name' as the index
print(df_indexed.loc["Charizard":"Pikachu", ["Height", "Weight"]])

# Selection By Index Position
print(df.iloc[0])  # Selecting a single row by index position
print(df.iloc[0:3])  # Selecting multiple rows by index position
print(df.iloc[0:3, 1:3])  # Selecting multiple rows and columns by index position
