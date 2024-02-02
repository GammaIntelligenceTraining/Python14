contact_book = {}

def add_contact(name, phone, email, **kwargs):
    if name not in contact_book:
        contact_book[name] = {
            'phone': phone,
            'email': email,
            # **kwargs
        }
        contact_book[name].update(kwargs)
        print(kwargs)
        print(f'Contact {name} was successfully added.')
    else:
        print(f'Contact {name} already exists!')


def view_contact(name):
    if name in contact_book:
        contacts = contact_book[name]
        print(f'Name: {name}, Phone: {contacts["phone"]}, Email: {contacts["email"]}')
    else:
        print(f'Contact {name} does not exist.')


def update_contact(name, phone, email):
    if name in contact_book:
        contact_book[name] = {'phone': phone, 'email': email}
        # contact_book[name].update({'phone': phone, 'email': email})
        # contact_book.update({name: {'phone': phone, 'email': email}})
        print(f'Contact {name} was successfully updated.')
    else:
        print(f'Contact {name} does not exist.')


def delete_contact(name):
    if name in contact_book:
        # contact_book.pop(name)
        del contact_book[name]
        print(f'Contact {name} was successfully deleted.')
    else:
        print(f'Contact {name} does not exist.')


add_contact('Roman', 1, 1, gender='Male', address='Tartu mnt. 18')
add_contact('Roman', 1, 1)

print('CONTACT', contact_book)
del contact_book['Roman']['address']
print('CONTACT', contact_book)
update_contact('Roman', 2, 2)
delete_contact('Bob')
view_contact('Roman')
