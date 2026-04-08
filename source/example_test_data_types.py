import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv('data/books_columns_renamed.csv')

df = prepare_data(df)

df.info()