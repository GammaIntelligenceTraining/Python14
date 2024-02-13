# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def squares(number):
#     return number ** 2
#
# new_nums = map(squares, numbers)
# # new_nums = []
# # for num in numbers:
# #     new_nums.append(squares(num))
# #
# print(list(new_nums))

# x = {
#     '2134dsasad131': {
#         'make': 'VW',
#         'model': 'Golf',
#     }
# }

# def change_dict(d):
#     make, model, serial = d['make'], d['model'], d['serial']
#     return {
#         serial: {
#             'make': make,
#             'model': model
#         }
#     }
#
# cars = [
#     {
#         'make': 'VW',
#         'model': 'Golf',
#         'serial': '2134dsasad131'
#     },
#     {
#         'make': 'BMW',
#         'model': '320i',
#         'serial': '2as1234dsvbd131'
#     },
#     {
#         'make': 'Seat',
#         'model': 'Leon',
#         'serial': 'sa23kmm322133'
#     }
# ]
#
# new_cars = map(change_dict, cars)
# print(list(new_cars))

# def power(a, b):
#     return a * b
#
nums1 = [3, 8, 8, 0, 3, 1, 6, 0, 2, 7, 2]
# nums2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
# new = map(power, nums1, nums2)
# print(sum(list(new)) % 11)

# def odd_or_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# new = filter(odd_or_even, nums1)
# print(list(new))

# data1 = [1, 2, 3, 4, 5]
# data2 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
#
# new = zip(data1, data2, data2, data1, range(10))
# print(list(new))