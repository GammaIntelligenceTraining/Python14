data = [1, 2, 3, 4, 5, 6, 7]
data2 = ['A', 'B', 'C', 'D', 'E', 'F']

# print(list(enumerate(data2, 100)))
zipped = zip(data, data2, data2, range(100))
print(list(zipped))