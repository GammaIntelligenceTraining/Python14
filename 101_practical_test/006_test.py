# 6 *Написать программу, которая для произвольного списка находит число / числа,
#    наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#     Примеры:
#     [1, 2, 3, 4, 7, 9, 9] → [9]
#     [1, 2, 4, 6, 4, 6] → [4,6]

test_lst = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7]

counts = {}
result = []

for num in test_lst:
    counts[num] = test_lst.count(num)

for key in counts.keys():
    if counts[key] == max(counts.values()):
        if key not in result:
            result.append(key)
print(result)

# max_count = 0
# result = []
# for num in test_lst:
#     if test_lst.count(num) > max_count:
#         max_count = test_lst.count(num)
#
# for num in test_lst:
#     if test_lst.count(num) == max_count:
#         if num not in result:
#             result.append(num)
#
# # result = list(set(result))
# print(result)