# 'r' - read
# 'w' - write
# 'x' - create
# 'a' - append
# 'r+' - read/write

# Absolute path
# C:\Users\User\PycharmProjects\Python14\007_working_with_files\text_files\tester.txt
# Relative path
# 007_working_with_files/text_files/tester.txt

# file = open('text_files/tester.txt', 'r', encoding='utf8')
# print(file.closed)
# file.close()
# print(file.closed)

# with open('text_files/tester.txt', 'r', encoding='utf8') as file:
#     # data = file.read()  # string
#     # data = file.readlines()  # list
#     data = file.readline()
#     file.write('Hello world!')
#
# print(data)

# with open('text_files/tester.txt', 'r', encoding='utf8') as file:
#     data = file.read()
# with open('text_files/tester.txt', 'w', encoding='utf8') as file:
#     file.write(data.upper())

# with open('text_files/python_picture.jpg', 'rb') as file:
#     with open('python_copy.png', 'wb') as wfile:
#         chunk_size = 4096
#         data = file.read(chunk_size)
#         while len(data) > 0:
#             wfile.write(data)
#             data = file.read(chunk_size)

with open('text_files/python_picture.jpg', 'rb') as file:
    with open('python_copy.png', 'wb') as wfile:
        chunk_size = 20096
        data = file.read(chunk_size)
        wfile.write(data)
