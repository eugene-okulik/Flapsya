my_dict = {
    'tuple': (False, 'Hello', 42, 15.2, None, 'QA'),
    'list': [4, 'value', 'asdasda', True, 85.9, 'lsdkjlsdfgjsdfl'],
    'dict': {'key': 'value', 150: 'yes', 'price': (50, 13, 20, 50.2, None), 85: 19, 'vault': True},
    'set': {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
}


#  Для того, что хранится под ключом ‘tuple’
last_element_tuple = my_dict['tuple'][-1]
print(last_element_tuple)


#  Для того, что хранится под ключом ‘list’
my_dict['list'].append('Last element')
my_dict['list'].pop(1)


#  Для того, что хранится под ключом ‘dict’
my_dict['dict'][(str('i am a tuple',))] = 'test'
my_dict['dict'].pop(150)


#  Для того, что хранится под ключом ‘set’
my_dict['set'].add(18)
my_dict['set'].remove(None)


print(my_dict)
