import json
# json_data = """{
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false,
#       "salary": 1500
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true,
#       "salary": 1700
#     },
#     {
#       "name": "Steven Cooke",
#       "phone": null,
#       "emails": "stevencooke@example.com",
#       "has_licence": true,
#       "salary": 2500
#     }
#   ]
# }"""
# data = json.loads(json_data)
# print(data)
# print(type(data))
# print(data['people'][0]['emails'])
#
# json_str = json.dumps(data, indent=2)
# print(json_str)
# print(type(json_str))

with open('sample2.json', 'r', encoding='utf8') as file:
    data = json.load(file)


for person in data['people']:
    if person['has_licence'] == False:
        data['people'].remove(person)


with open('sample2_copy.json', 'a', encoding='utf8') as file:
    json.dump(data, file, indent=2)


with open('data.json', 'r', encoding='utf') as file:
    json.load(file)