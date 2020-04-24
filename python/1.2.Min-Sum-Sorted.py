#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away

#                                   NUMBER OF ITEMS
# Find the minumum item in a sequence lexicographically.
# Alpha or numeric types, but cannot mix types.

# String
x = 'orange'
print('Min value of x:', min(x))

# List
y = ['apple', 'banana', 'guava']
print('Min value of y:', min(y))

# Tuple
z = ('Jhon', 'Oscar', 'Steve')
print('Min value of z:', min(z))

#                                       SUM
print('\n')

# Sum a same type of items

# List
y = [1, 9, 4, 6]
print('Sum y:', sum(y))
print('Sum without last 2 items:', sum(y[-2:]))

# Tuple
z = [11, 15, 2, 16]
print('Sum z:', sum(z))

#                                      SORTING
print('\n')
# Returns a new list of items in sorted order
# Doesn't change the original list

# String
x = 'orange'
print('Sorted x:', sorted(x))

# List
y = ['apple', 'banana', 'guava']
print('Sorted y:', sorted(y))

# Tuple
z = ('Jhon', 'Oscar', 'Steve')
print('Sorted z:', sorted(z))

# Sorting by Second Letter
# Add a key parameter and a lambda function to return the second character.
# (key is an arbitrary name)

z = ('Jhon', 'Oscar', 'Steve', 'Cartman')
print('Sorted by 2nd letter: ', sorted(z, key=lambda k: k[1]))
