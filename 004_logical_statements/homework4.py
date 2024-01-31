# # Дан список, каждый элемент которого является годом. Определите, является ли данный год високосным.
# # Если год является високосным, выведите YES, иначе выведите NO.
# # В соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100
# # ИЛИ если он кратен 400.
# years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
# # for year in years_list:
# #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# #         print(year, 'Yes')
# #     else:
# #         print(year, 'No')
#
# # Даны три переменных, каждая из которых может принимать значение True или False
# # Напишите код, который выдает True, если хотя бы 2 из 3 переменных имеют значение True
# # Код должен работать для любых возможных сочетаний значений переменных.
# var1 = True
# var2 = False
# var3 = True
# if var1 and var2 or var1 and var3 or var3 and var2:
#     print('True')
#
# # print(var1 + var2 + var3 >= 2)
# x = input('Enter something: ')
# if x:
#     print(x)
# else:
#     print('Nothing')
#
#
# # Напишите программу, запрашивающую у пользователя строку и проверяющую
# # содержит ли данная строка только уникальные символы
# user_input = input('Enter some text: ')
#
# for letter in user_input:
#     if user_input.count(letter) > 1:
#         print('There are non unique characters')
#         break
#     else:
#         print(letter, 'is unique')
#         continue
#
#
# # if user_input:
# #     for letter in user_input:
# #         if user_input.count(letter) > 1:
# #             unique = False
# #     if unique:
# #         print('String has unique characters only')
# #     else:
# #         print('There are non unique characters')
# # else:
# #     print('You didn\'t enter anything.')
#
#
#
# # Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary", "car"]
#
# for key in keys:
#     if key in sample_dict:
#         del sample_dict[key]
#         # deleted = sample_dict.pop(key)
# print(sample_dict)
#
#
# # You have a dictionary with keys 'names' and 'ages' and two empty lists as values.
# # Fill these lists with the elements from the set ('names' for strings, 'ages' for integers)
# d = {'names': [], 'ages': []}
# s = {14, 27, 'Michel', 22, 'Helen', 'Adam', 48, 'Irma', 'Stefan', 19}
# for value in s:
#     if type(value) == str:
#         d['names'].append(value)
#     elif type(value) == int:
#         d['ages'].append(value)
#     else:
#         print('Unknown data!')
#
# print(d)


x = {
    'name': 'Jack',
    'contacts': {
        'emails': [
            'jack@example.com',
            'jack@company.com'
        ],
        'phone': '555-555-5555'
    },
    'info': [
        'Brown eyes',
        '180cm tall',
        '80kg weight'
    ]
}
y = x['contacts']['emails']
print(x['contacts']['emails'][1][4:8].upper()[0])

