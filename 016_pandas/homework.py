import pandas as pd

'''
Домашнее задание:
Для опроса на Stack Overflow (https://insights.stackoverflow.com/survey) (017_pandas/csv_files/survey_results_public.csv)
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке возрастания
'''

# https://tproger.ru/digest/data-science-python/#1

data = pd.read_csv('csv_files/survey_results_public.csv')

# print(data['Hobbyist'].value_counts())
# print(data.groupby('Hobbyist').count()['Respondent'])
#

# print('Max', data['Age'].max())
# print('Mean', data['Age'].mean())
# print('Min', data['Age'].min())

#
# print(data['Country'].value_counts(ascending=False))
# print(data.groupby('Country').count().sort_values('Respondent', ascending=False)['Respondent'])


print(data['CurrencyDesc'].value_counts(ascending=True))
print(data.groupby('CurrencyDesc').count().sort_values('Respondent')['Respondent'])