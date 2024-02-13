import itertools

def get_city(person):
    return person['city']

people = [
    {
        'name': 'Jack',
        'city': 'Berlin'
    },
    {
        'name': 'Mary',
        'city': 'Berlin'
    },
    {
        'name': 'Sarah',
        'city': 'Berlin'
    },
    {
        'name': 'Bob',
        'city': 'Tallinn'
    },
    {
        'name': 'Jessica',
        'city': 'Tallinn'
    },
    {
        'name': 'Simon',
        'city': 'Tallinn'
    },
    {
        'name': 'Roger',
        'city': 'Berlin'
    },
]
people.sort(key=get_city)
result = itertools.groupby(people, get_city)

copy1, copy2 = itertools.tee(result)

for key, group in copy1:
    print(key)
    for person in group:
        print(person)