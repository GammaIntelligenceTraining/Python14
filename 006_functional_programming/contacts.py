"""
'name': {'phone': ********, 'email': *******}
add contact (name, phone, email)
view contact (name)
update contact (name, phone, email)
delete contact (name)
list contacts
"""
contact_book = {}

def add_contact(name, phone, email, **kwargs):
    if name not in contact_book:
        contact_book[name] = {'phone': phone, 'email': email}
        contact_book[name].update(kwargs)
        print(f'Contact {name} was updated.')
    else:
        print(f'Contact {name} already exists.')


def view_contact(name):
    if name in contact_book:
        print(name)
        for key, value in contact_book[name].items():
            print(f'\t{key.title()}: {value}')
    else:
        print(f'Contact {name} does not exists.')


def update_contact(name, phone=None, email=None, **kwargs):
    if name in contact_book:
        data = {**kwargs}
        if phone:
            data['phone'] = phone
        if email:
            data['email'] = email
        contact_book[name].update(data)
        print(f'Contact {name} was updated.')
    else:
        print(f'Contact {name} does not exist.')


def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f'Contact {name} was deleted.')
    else:
        print(f'Contact {name} does not exist.')


def list_contacts():
    contact_list = list(contact_book.keys())
    contact_list.sort()
    contact_list = enumerate(contact_list, 1)
    for num, name in contact_list:
        print(f'{num}.{name}')



add_contact('Roman', '555-55555', 'roman@example.com', address='Tartu mnt. 18', height=179)
add_contact('Jack', '555-55555', 'roman@example.com')
add_contact('Mary', '555-55555', 'roman@example.com')
add_contact('Sarah', '555-55555', 'roman@example.com')
add_contact('Jessica', '555-55555', 'roman@example.com')
add_contact('George', '555-55555', 'roman@example.com')
# view_contact('Roman')
# update_contact('Roman', '123213123')
# delete_contact('Roman')
list_contacts()
print(contact_book)





# x = {'name': 'Jack'}
# print(x['name'])
# del x['name']
# print(x['name'])