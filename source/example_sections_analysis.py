import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv('data/books_columns_renamed.csv')

df = prepare_data(df)

inventory_gap = df.groupby('section').agg({
    'title': 'count',
    'times_borrowed': 'sum'
})

inventory_gap['titles_to_borrow_ratio'] = inventory_gap['times_borrowed'] / inventory_gap['title']

print(inventory_gap.sort_values(by=['titles_to_borrow_ratio'], ascending=False))


