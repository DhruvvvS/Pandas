# Pandas Series Basics

# Series = One-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
#          The axis labels are collectively referred to as the index. A Series is like a fixed-size dictionary in that you can get and set values by index label.
#          Think of it as a column in an Excel spreadsheet or a SQL table. It is the primary building block of Pandas.
#          unlike a plain Python list, you can look up a value by its label,not just its position.

import pandas as pd

data = [100, 200, 300, 400, 500]

series = pd.Series(data)

# Series can be created from a list, dictionary, or scalar value. The index can be specified explicitly or will default to a range of integers.
# Also at the end of the series, you can see the data type of the series.
print(series)

# Series constructor can also take index as an argument
index = ["a", "b", "c", "d", "e"]
series_with_index = pd.Series(data, index=index)
print(series_with_index)

# .loc is a label-based indexer for selecting rows and columns by their labels. It allows you to access data in a Series or DataFrame using the index labels.
print(series_with_index.loc["c"])  # Accessing value by label 'c'
# If a label does not exist in the index, it will raise a KeyError.

# .loc can also be used to access multiple values by passing a list of labels.
print(series_with_index.loc[["a", "c", "e"]])  # Accessing multiple values by labels 'a', 'c', and 'e'

# .loc can also be used to change the value of a specific label in the Series.
series_with_index.loc["b"] = 250  # Changing the value of label 'b'
print(series_with_index)

# .iloc is an integer-location based indexer for selecting rows and columns by their integer position. It allows you to access data in a Series or DataFrame using the integer index.
print(series_with_index.iloc[2])  # Accessing value by integer position 2 (which corresponds to label 'c')
# If an integer position does not exist in the index, it will raise an IndexError.

print(series_with_index.iloc[[0, 2, 4]])  # Accessing multiple values by integer positions 0, 2, and 4

print(series[series>=300])  # Filtering values greater than or equal to 300
# We can also use boolean indexing to filter the Series based on a condition. The result will be a new Series containing only the values that meet the condition.
