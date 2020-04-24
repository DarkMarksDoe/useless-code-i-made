#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away

#                                   COUNT(ITEM)

# String
x = 'trichotillomania'
print('There are', x.count('i'), 'i in x')

# List
y = ['apple', 'banana', 'guava', 'apple']
print('There are:', y.count('apple'), 'apples in y')

# Tuple
z = ('Jhon', 'Oscar', 'Steve', 'Cartman')
print('There is:', z.count('Oscar'), 'Oscar in z')

#                                   INDEX(ITEM)
print('\n')
# Return the index of an item
# String

x = 'orange'
print('o is in position:', x.index('o'), 'in', x)

# List
y = ['apple', 'banana', 'guava']
print('banana is in position:', y.index('banana'), 'in', y)

# Tuple
z = ('Jhon', 'Oscar', 'Steve')
print('Steve is in position:', z.index('Steve'), 'in', z)

#                                   UNPACKING(ITEM)
print('\n')
# Unpack n items into n variables

y = ['apple', 'banana', 'guava']
a, b, g = y
print(a, b, g)
