# Using dictionart to create a Series
# Pizza calorie counter example

import pandas as pd

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1850}
series = pd.Series(calories)
# We don't need to specify the index here because the keys of the dictionary will automatically be used as the index for the Series.

print(series)

print(series["Day 2"])  # Accessing value by label 'Day 2'

series["Day 3"] = 1900  # Changing the value of label 'Day 3'
series.loc["Day 1"] += 200  # Adding 200 to the value of label 'Day 1' using .loc
print(series)

print(series[series > 2000])  # Filtering values greater than 2000