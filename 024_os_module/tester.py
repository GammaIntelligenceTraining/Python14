import os
import time

# # os.mkdir('temp/new1')
# os.makedirs('temp/new1/new2/new3')
# time.sleep(10)
# # os.rmdir('temp/new1/new2/new3')
# os.removedirs('temp/new1/new2/new3')

# print(os.stat('tester.py'))

# information = os.walk('../')
# # print(information)
#
# for dirpath, dirnames, filenames in information:
#     print('*' * 20)
#     print('Current path', dirpath)
#     print('Directories', dirnames)
#     print('Files', filenames)
#     print()

# print(os.environ.get('HOMEPATH'))

# p = 'C:\\Users\\User'
# file = 'test.txt'
# path = os.path.join(p, file)
# print(path)
#
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.splitext(path))
# print(os.path.split(path))

# print(os.path.exists('../022_flask'))
# print(os.path.isdir('tester2'))
# print(os.path.isfile('../'))
# print(os.path.splitdrive('Users\\Hello\\new folder'))

os.rename('sample.txt', 'tester/some_text.txt')
