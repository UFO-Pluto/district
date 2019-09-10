import pandas as pd
import numpy as np

pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)

df = pd.read_csv('data.csv',index_col='id')
df = df.replace(np.nan, '', regex=True)

print(df)

for index, row in df.iterrows():
    # province
    if row['父id'] == 0:
        if row['附加说明']:
            fj = row['附加说明']
        else:
            fj = ''
        if row['行政级别']:
            jb = row['行政级别']
        else:
            jb = ''
        name = row['名称'] + fj + jb
        print(name)
        print(row['行政代码'])
    # city
    if row['父id'] != 0:
        # print(row['名称'])
        # print(row['父id'])
        # print(df.loc[row['父id'], '名称'])
        if df.loc[row['父id'], '父id'] == 0:
            if row['附加说明']:
                fj = row['附加说明']
            else:
                fj = ''
            if row['行政级别']:
                jb = row['行政级别']
            else:
                jb = ''
            name = row['名称'] + fj + jb
            print(name)
            print(row['行政代码'])




