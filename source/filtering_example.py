import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv('data/books_columns_renamed.csv')

df = prepare_data(df)

df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce')

mask = (df['genre'] == 'Science') & (df['total_copies'] < 4)

filtered_books = df[mask]

print(filtered_books[['title', 'total_copies']])

