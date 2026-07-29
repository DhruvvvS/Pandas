# Pandas Aggregation Basics

# Aggregation = The process of performing calculations on a pandas DataFrame to summarize or derive insights from the data.
#               Reduces set of values into a single summary value.              

# Pandas provides several methods for aggregation, including .sum(), .mean(), .count(), .min(), .max(), and more.  

import pandas as pd
df = pd.read_csv("F:/Git/Pandas/Datasets/data.csv")  # Importing a CSV file into a DataFrame

# Aggregation Methods for whole dataframe
print(df.mean(numeric_only=True))  # Calculating the mean of all numeric columns in the DataFrame
print(df.sum(numeric_only=True))  # Calculating the sum of all numeric columns in the DataFrame
print(df.count())  # Calculating the count of all columns in the DataFrame
print(df.min(numeric_only=True))  # Calculating the minimum value of all numeric columns in the DataFrame
print(df.max(numeric_only=True))  # Calculating the maximum value of all numeric columns in the DataFrame

# Aggregation Methods for specific columns
print(df["Height"].mean())  # Calculating the mean of the 'Height' column
print(df["Weight"].sum())  # Calculating the sum of the 'Weight' column

# Aggregation Methods for specific rows
print(df.loc[0, df.select_dtypes(include="number").columns].mean())  # Calculating the mean of the first row

# Aggregation Methods with Grouping
grouped_df = df.groupby("Type1")  # Grouping the DataFrame by the 'Type1' column
print(grouped_df["Height"].mean())  # Calculating the mean of the 'Height' column for each group in 'Type1' 
print(grouped_df["Weight"].sum())  # Calculating the sum of the 'Weight' column for each group in 'Type1'
print(grouped_df["Name"].count())  # Calculating the count of the 'Name' column for each group in 'Type1'

# Aggregation Methods with Multiple Aggregations
agg_df = grouped_df.agg({"Height": "mean", "Weight": "sum", "Name": "count"})  # Performing multiple aggregations on the grouped DataFrame
print(agg_df)  # Displaying the aggregated DataFrame with mean of 'Height', sum of 'Weight', and count of 'Name' for each group in 'Type1'

# Aggregation Methods with Custom Functions
def range_func(x):
    return x.max() - x.min()  # Custom function to calculate the range (max - min) of a series
print(grouped_df["Height"].apply(range_func))  # Calculating the range of the 'Height' column for each group in 'Type1'

# Aggregation Methods with Lambda Functions
print(grouped_df["Weight"].apply(lambda x: x.max() - x.min()))  # Calculating the range of the 'Weight' column for each group in 'Type1'

# Aggregation Methods with Transformations
print(grouped_df["Height"].transform("mean"))  # Transforming the 'Height' column to have the mean value for each group in 'Type1' while maintaining the original DataFrame shape    

# Aggregation Methods with Pivot Tables
pivot_table_df = df.pivot_table(index="Type1", values=["Height", "Weight"], aggfunc={"Height": "mean", "Weight": "sum"})  # Creating a pivot table to summarize 'Height' and 'Weight' by 'Type1'
print(pivot_table_df)  # Displaying the pivot table with mean of 'Height' and sum of 'Weight' for each group in 'Type1'
