
#!                               COURSE DATA STRUCTURES

#*               Native Python Data Structures, Operators for Sequence
#*               Types like: Strings, List, Tuples
#?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

#* If this code works, it was written by DarkMarksDoe. If not, I don't know
#* who wrote it, just pass away


#TODO INFO ABOUT DICTIONARIES

#* Key/Value pairs
#* Associative array, like Java HashMap
#* Dicts are Unordered

#!                                     CONSTRUCTORS
print('\n')
x = {
    'pork': 25.3,
    'beef': 33.8,
    'chicken': 22.7
}
print('Normal Map:', x)

#? Parse from list of tuples
x = dict(
    [
        ('pork', 25.3),
        ('beef', 33.8),
        ('chicken', 22.7)
    ]
)
print('Parse Map from List of Tuples:', x)

#? Parse list of declarations
x = dict(
    pork=25.3,
    beef=33.8,
    chicken=22.7
)
print('Parse Map from declarations:', x)

#!                                DICT OPERATIONS
print('\n')

#? Add or Update an item
x['shrimp'] = 38.2
print('Add:', x)

#? Delete an item
del(x['shrimp'])
print('Delete:', x)

#? Delete all items from dict x
x.clear()
print('Clear:', x)

#? Delete dict x
del(x)

#!                              ACCESING KEYS AND VALUES IN A DICT
print('\n')

y = {
    'pork': 25.3,
    'beef': 33.8,
    'chicken': 22.7
}
#? Get  keys
print('Keys of y:', y.keys())
#? Get  values
print('Values of y:', y.values())
#? Get  items
print('Items of y:', y.items())

#? Check Membership in y_keys (only looks in keys, not values)
print('Membership Keys:', 'beef' in y)

#? Check Membership in y_values
print('Membership Values:', 'clams' in y)

#!                              ITERATING A DICT
print('\n')

#? Print enumerated key and their values
for index, item in enumerate(y):
    print('key ', index, ':', item, ', value:', y[item])

#? Print value and key from y.items
for k, v in y.items():
    print(k, v)

my_list = [20, 10, 25, 35]
count = len(my_list)
print(count)