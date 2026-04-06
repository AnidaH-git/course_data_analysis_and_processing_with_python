import pandas as pd

df = pd.read_csv('data/books.csv')

df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]

df.to_csv('data/books_columns_renamed.csv', index=False, encoding="utf-8")
