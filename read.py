import pandas as pd
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)

df = pd.read_csv('data.csv')
print(df)