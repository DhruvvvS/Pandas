# Pandas Filtering Basics

# Filtering = The process of selecting specific rows from a pandas DataFrame based on certain conditions or criteria.

import pandas as pd

df = pd.read_csv("F:/Git/Pandas/Datasets/data.csv")  # Importing a CSV file into a DataFrame

tall_pokemon = df[df["Height"] > 3.0]  # Filtering rows where the 'Height' column is greater than 3.0
print(tall_pokemon)  # Displaying the filtered DataFrame

heavy_pokemon = df[df["Weight"] > 150.0]  # Filtering rows where the 'Weight' column is greater than 150.0
print(heavy_pokemon)  # Displaying the filtered DataFrame

# Filtering with Multiple Conditions
tall_and_heavy_pokemon = df[(df["Height"] > 3.0) & (df["Weight"] > 150.0)]  # Filtering rows where 'Height' is greater than 3.0 AND 'Weight' is greater than 150.0
print(tall_and_heavy_pokemon)  # Displaying the filtered DataFrame

# Filtering with OR Condition
ff_pokemon = df[(df["Type1"] == "Fire") | (df["Type2"] == "Flying")]  # Filtering rows where 'Type1' is 'Fire' OR 'Type2' is 'Flying'
print(ff_pokemon)  # Displaying the filtered DataFrame
