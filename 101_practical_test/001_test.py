# 1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#     Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

first_name = input('Enter name: ')
last_name = input('Enter surname: ')
age = input('Enter age: ')

print(f'Hello, {last_name.title()} {first_name.title()}. Your age is: {age}')