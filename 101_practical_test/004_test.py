# 4 Пользователь вводит некоторый произвольный список list.
# Написать программу, выводящую элементы списка в обратном порядке.

user_entry = input('Enter some elements. Use ", " as separator: ').split(', ')
for value in user_entry[::-1]:
    print(value)
