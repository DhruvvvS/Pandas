# Pandas file importing basics

# Importing = The process of loading data from various file formats into a pandas DataFrame for analysis and manipulation.
#             Pandas provides several functions to import data from different file formats, such as CSV, Excel, JSON, SQL databases, and more. 

# We will be importing a CSV file in this example. CSV (Comma-Separated Values) is a common file format used for storing tabular data from our datasets.

import pandas as pd

# The read_csv() function is used to read a CSV file and create a DataFrame. It takes the file path as an argument and returns a DataFrame containing the data from the CSV file.
df_csv = pd.read_csv("F:/Git/Pandas/Datasets/data.csv")  # Importing a CSV file into a DataFrame
print(df_csv)

# .tostring() method is used to convert the DataFrame into a string representation for display purposes. It provides a tabular view of the DataFrame, making it easier to visualize the data.
print(df_csv.to_string())  # Displaying the DataFrame as a string representation
# Showing data of entire 150 rows of the DataFrame. If the DataFrame has more than 60 rows, it will display the first 30 and last 30 rows by default.

# We will be importing an JSON file in this example. JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

# The read_json() function is used to read a JSON file and create a DataFrame. It takes the file path as an argument and returns a DataFrame containing the data from the JSON file.
df_json = pd.read_json("F:/Git/Pandas/Datasets/data.json")  # Importing a JSON file into a DataFrame
print(df_json)

# .tostring() method is used to convert the DataFrame into a string representation for display purposes. It provides a tabular view of the DataFrame, making it easier to visualize the data.
print(df_json.to_string())  # Displaying the DataFrame as a string representation
# Showing data of entire 150 rows of the DataFrame. If the DataFrame has more than 60 rows, it will display the first 30 and last 30 rows by default.

# FOR DIFFERENT FILE FORMATS

# excel = pd.read_excel("F:/Git/Pandas/Datasets/data.xlsx")  # Importing an Excel file into a DataFrame
# sql = pd.read_sql("SELECT * FROM table_name", connection)  # Importing data from a SQL database into a DataFrame
# parquet = pd.read_parquet("F:/Git/Pandas/Datasets/data.parquet")  # Importing a Parquet file into a DataFrame
# html = pd.read_html("F:/Git/Pandas/Datasets/data.html")  # Importing an HTML file into a DataFrame
# xml = pd.read_xml("F:/Git/Pandas/Datasets/data.xml")  # Importing an XML file into a DataFrame
# hdf = pd.read_hdf("F:/Git/Pandas/Datasets/data.h5")  # Importing an HDF5 file into a DataFrame
# feather = pd.read_feather("F:/Git/Pandas/Datasets/data.feather")  # Importing a Feather file into a DataFrame
