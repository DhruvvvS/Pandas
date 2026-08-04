# Pandas Data Cleaning Basics

# Data Cleaning = The process of identifying and correcting errors, inconsistencies, and inaccuracies in a dataset to ensure its quality and reliability for analysis.

import pandas as pd
df = pd.read_csv("F:/Git/Pandas/Datasets/data.csv")  # Importing a CSV file into a DataFrame

# Dropping Irrelevant Columns
df_cleaned = df.drop(columns=["Legendary"])  # Dropping the 'Legendary' column from the DataFrame
print(df_cleaned.head())  # Displaying the first few rows of the cleaned DataFrame

# Handling Missing Values
df_cleaned = df_cleaned.dropna()  # Dropping rows with any missing values
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

df_cleaned = df_cleaned.dropna(subset=["Height"])  # Dropping rows with missing values in the 'Height' column
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

df_cleaned = df_cleaned.fillna(0)  # Filling missing values with 0
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

df_cleaned = df_cleaned.fillna({"Type2": "None"})  # Filling missing values in the 'Type2' column with 'None'
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

# Fixing inconsistent values
df_cleaned["Type1"] = df_cleaned["Type1"].str.capitalize()

df_cleaned["Type1"] = df_cleaned["Type1"].replace({"Fire": "Flame", "Water": "Aqua"})  # Replacing inconsistent values in the 'Type1' column
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

# Fixing data types
df_cleaned["Height"] = df_cleaned["Height"].astype(float)  # Converting the 'Height' column to float data type
df_cleaned["Weight"] = df_cleaned["Weight"].astype(float)  # Converting the 'Weight' column to float data type
print(df_cleaned.dtypes)  # Displaying the data types of the cleaned DataFrame

# Removing duplicates
df_cleaned = df_cleaned.drop_duplicates()  # Dropping duplicate rows from the Dataframe
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

# Renaming columns
df_cleaned = df_cleaned.rename(columns={"Type1": "Primary_Type", "Type2": "Secondary_Type"})  # Renaming columns for clarity
print(df_cleaned.to_string())  # Displaying the rows of the cleaned DataFrame

# Saving the cleaned DataFrame to a new CSV file
df_cleaned.to_csv("F:/Git/Pandas/Datasets/cleaned_data.csv", index=False)  # Saving the cleaned DataFrame to a new CSV file without the index
