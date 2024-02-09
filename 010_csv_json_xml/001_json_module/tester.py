import json
# json_string = '''
# {
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true
#     }
#   ]
# }'''
# data = json.loads(json_string)
#
# # print(type(data))
# # print(data['people'])
# #
# # for person in data['people']:
# #     print(person['name'], person['phone'])
#
# data['people'].append({
#         'name': 'Robert Brown',
#         'phone': '222-555-5555',
#         'emails': 'robert@example.com',
#         'has_licence': True
#     })
# print(data)
# print(type(data))
#
# new_json = json.dumps(data, indent=2)
# print(new_json)
# print(type(new_json))

with open('sample2.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data))

data['people'].append({
        'name': 'Robert Brown',
        'phone': '222-555-5555',
        'emails': 'robert@example.com',
        'has_licence': True
    })

with open('sample2_edited.json', 'w') as file:
    json.dump(data, file, indent=2)

