import csv

# with open('csv_files/test.csv', 'r', encoding='utf8') as file:
#
#     csv_data = csv.reader(file)
#
#     with open('csv_files/test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.writer(wfile, delimiter=',', lineterminator='\n', quotechar='*')
#
#         csv_writer.writerows(csv_data)
#         # for line in csv_data:
#         #     csv_writer.writerow(line)
#
# with open('csv_files/test_copy.csv', 'r', encoding='utf8') as file:
#     csv_data = csv.reader(file, delimiter=',', lineterminator='\n')
#
#     for line in csv_data:
#         print(line)

with open('csv_files/test.csv', 'r', encoding='utf8') as file:
    headers = ['N', 'D', 'T']
    csv_reader = csv.DictReader(file)

    with open('csv_files/test_copy.csv', 'w', encoding='utf8') as wfile:
        csv_writer = csv.DictWriter(wfile, fieldnames=['Name', 'Date of birth', 'Town'], lineterminator='\n')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

with open('csv_files/test_copy.csv', 'a', encoding='utf8') as wfile:
    csv_writer = csv.DictWriter(wfile, fieldnames=['Name', 'Date of birth', 'Town'], lineterminator='\n')
    data = [{'Name': 'Roman', 'Date of birth': '16.03.88', 'Town': 'Tallinn'},
            {'Name': 'Marie', 'Date of birth': '13.01.94', 'Town': 'London'}]
    csv_writer.writerows(data)
