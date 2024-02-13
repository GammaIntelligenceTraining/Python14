def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

def infinite_counter(start):
    while True:
        start += 1
        yield start - 1

# y = infinite_counter(0)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# for i in y:
#     print(i)


# x = squares_generator(1, 100)
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# for i in x:
#     print(i)