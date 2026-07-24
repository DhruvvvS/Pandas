# Pandas Dataframes Basics

# DataFrame = A tabular data structure with labeled rows and columns. It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
#             It is generally the most commonly used pandas object.

import pandas as pd

# DataFrame can be created from a dictionary, list of dictionaries, or a 2D array. The index can be specified explicitly or will default to a range of integers.
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)
print(df)

# DataFrame constructor can also take index as an argument.
index = ["a", "b", "c", "d", "e"]
df_with_index = pd.DataFrame(data, index=index)
print(df_with_index)

# .loc is a label-based indexer for selecting rows and columns by their labels. It allows you to access data in a DataFrame using the index labels.
print(df_with_index.loc["c"])  # Accessing row by label 'c'
# If a label does not exist in the index, it will raise a KeyError and it also gives label name at the end.

# .iloc is an integer-location based indexer for selecting rows and columns by their integer position. It allows you to access data in a DataFrame using the integer index.
print(df_with_index.iloc[2])  # Accessing row by integer position 2 (which corresponds to label 'c')
# If an integer position does not exist in the index, it will raise an IndexError and it also gives the integer position at the end. 

# You can also select specific columns using .loc and .iloc.
print(df_with_index.loc["b", "Name"])  # Accessing specific value by row label 'b' and column label 'Name'
print(df_with_index.iloc[1, 0])  # Accessing specific value by row integer position 1 and column integer position 0

# You can also select multiple rows and columns using .loc and .iloc.
print(df_with_index.loc[["a", "c", "e"], ["Name", "City"]])  # Accessing multiple rows and columns by labels
print(df_with_index.iloc[[0, 2, 4], [0, 2]])  # Accessing multiple rows and columns by integer positions

# You can filter rows in a DataFrame based on a condition.
print(df_with_index[df_with_index["Age"] >= 35])  # Filtering rows where Age is greater than or equal to 35

# Add a new column to the DataFrame.
df_with_index["Country"] = ["USA", "USSR", "AUS", "IND", "FRA"]
print(df_with_index)

# Add a new row to the DataFrame using .loc.
df_with_index.loc["f"] = ["Frank", 50, "Miami", "USA"]
print(df_with_index)

# Add a new row to the DataFrame
new_row = pd.DataFrame({"Name": ["Grace"], "Age": [55], "City": ["Seattle"], "Country": ["USA"]}, index=["g"])
df_with_index = pd.concat([df_with_index, new_row])
print(df_with_index)

# You can also drop rows or columns from the DataFrame using the .drop() method.
df_dropped_row = df_with_index.drop("b")  # Dropping row with label 'b'
print(df_dropped_row)

# Dropping a column from the DataFrame
df_dropped_column = df_with_index.drop("Country", axis=1)  # Dropping column 'Country'
print(df_dropped_column)