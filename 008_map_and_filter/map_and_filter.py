x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd(num):
    if num % 2 == 0:
        return False
    return True

y = filter(odd, x)
print(list(y))

people = [
    {
        'name': 'Jack',
        'age': 15
    },
    {
        'name': 'Bob',
        'age': 21
    },
    {
        'name': 'Mary',
        'age': 20
    },
]

def is_adult(person):
    if person['age'] >= 18:
        return True
    return False

adults = list(filter(is_adult, people))
print(adults)

def squares(num):
    return {num: num ** 2}

squares_lst = list(map(squares, x))
print(squares_lst)


def adult_or_teenager(person):
    new_person = {
        **person
    }
    if person['age'] >= 18:
        new_person['status'] = 'adult'
    else:
        new_person['status'] = 'teenager'
    return new_person

people_extended = list(map(adult_or_teenager, people))
print(people_extended)


res = list(filter(lambda num: num % 2 == 0, x))
print(res)

test = lambda num1, num2: num1 * num2

print(test(10, 20))

res = list(map(lambda num: {num: num ** 2}, x))
print(res)

sample = [[1, 2], [5, 3], [3, 1], [4, 9]]

sample.sort(key=lambda x: x[1])
print(sample)