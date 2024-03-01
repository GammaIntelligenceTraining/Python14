import pandas as pd
import mysql.connector

df = pd.read_csv('csv_files/2019.csv')
pd.set_option('display.max_columns', 9)

# print(df.loc[df['Overall rank'] < 10])

# print(df.memory_usage(deep=True))
# print(df.dtypes)

# print(df.sort_values(['Country or region', 'Perceptions of corruption'], ascending=[False, True]))

# df['Total'] = df['GDP per capita'] + df['Score'] * 200
# print(df)
#
# df.insert(loc=1, column='NEW', value=(df['GDP per capita'] * 2))
# print(df)
#
# df = df.drop(columns=['Total', 'NEW'])
# print(df)

# print(df.loc[df['Country or region'].str.contains('o|a')])

# print(df.groupby('Country or region').mean()['GDP per capita'])

df1 = df.nlargest(5, 'GDP per capita')
# print(df1)
df2 = df.nsmallest(5, 'GDP per capita')
# print(df2)

df3 = pd.read_csv('csv_files/test.csv')
print(pd.concat([df1, df2, df3]))
