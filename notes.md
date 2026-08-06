# Pandas Notes

- Pandas is a Python Library built on top of NumPy
- Widely used in Data Analysis, Data Science and Machine Learning
- It is basically python's version of Microsoft Excel

## Series

- 1D labeled array. `pd.Series([1,2,3], index=['a','b','c'])`
- 1D labeled column

## DataFrame

- 2D table, dict of Series. `pd.DataFrame({'col1': [...], 'col2': [...]})`

## Importing

- `pd.read_csv('file.csv')`, `df.head()`, `df.info()`, `df.shape`
- `pd.read_json('file.json')`, `df.head()`, `df.info()`, `df.shape`

## Selection

- `df['col']` vs `df[['col1','col2']]`
- `df.loc[row_label, col_label]` — label-based
- `df.iloc[row_pos, col_pos]` — position-based

## Filtering

- `df[df['col'] > 5]`
- multiple conditions: `df[(cond1) & (cond2)]`

## Aggregation

- `df.groupby('col').mean()`, `.sum()`, `.agg([...])`

## Gotchas / things that tripped me up

- Selection with labeled index with .loc method
- Groupedof aggregation method
- Handling missing values in data cleaning

But not having any problems in solving.
