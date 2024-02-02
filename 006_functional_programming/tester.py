# def say_hello(name, surname):
#     print(f'Hello {name} {surname}!')
#
#
# def rectangle_area(a, b):
#     result = a * b
#     return result
#
# print((rectangle_area(60, 100) * 200) / 10000)
#
#
# print(rectangle_area(60, 70))
# area = rectangle_area(80, 90)
# print(area)
#
# def add_person(name):
#     people.append(name)
#
#
# people = []
#
# add_person('Jack')
# add_person('Mary')
# add_person('Sarah')
#
# print(people)


# odds = []
# evens = []
#
# def sort_numbers(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
#
# sort_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(odds)
# print(evens)

# def sort_numbers(num):
#     if num % 2 == 0:
#         return 'EVEN'
#     else:
#         return  'ODD'
#     print('DONE')
# def sum_three_or_two(a, b, c=100):
#     return a + b + c
#
#
# print(sum_three_or_two(10, 20))

# def say_hello(name=None, surname=None):
#     if name and surname:
#         print(f'Hello {name} {surname}!')
#     elif name and not surname:
#         print(f'Hello {name}!')
#     elif not name and surname:
#         print(f'Hello mr/mrs {surname}!')
#     else:
#         print(f'Hello stranger!')
#
# say_hello(surname='Kutselepa', name='Roman')

# def many_arguments(a, b, c=100, *args, **kwargs):
#     # print(args)
#     for arg in args:
#         print(arg)
#     print(kwargs)
#
# many_arguments(10, 20, 1, 'asd', [1,2,3], 123, 0.231, name='Jack', surname='Smith')

# x = [1, 2, 3]
# y = [0, *x, 4, 5, 6]
# print(y)


a, b, c = 10, 20, 30
def tester():
    global a, b
    a = 1
    b = 2

tester()
print(a, b, c)
