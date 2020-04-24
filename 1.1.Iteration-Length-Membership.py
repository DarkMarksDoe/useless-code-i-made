#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away

#                               MULTIPLY A SEQUENCE USING *
print('\n')

# String
x = 'bug' * 3
print('Multiply x by 3:', x)

# Listcls

y = [8, 5] * 3
print('\nMultiply y by 3:', y)

# Tuple
z = (2, 4) * 3
print('\nMultiply z by 3:', z)

#                                   CHECKING MEMBERSHIP
print('\n')

# String
x = 'bug'
print('u' in x)

# List
y = ['apple', 'banana', 'guava']
print('guava'not in y)

# Tuple
z = ('Jhon', 'Oscar', 'Steve')
print('Oscar' in z)

#                                        ITERATING
print('\n')

# item
x = [4, 2, 8]
for item in x:
    print('value:', item)

#index & item
y = [6, 1, 9]
for index, item in enumerate(y):
    print('Number', index, 'with value:', item)

#                                      NUMBER OF ITEMS
print('\n')

# String
x = 'bug'
print('Length of x:', len(x))

# List
y = ['apple', 'banana', 'guava']
print('Length of list:', len(y))

# Tuple
z = ('Jhon', 'Oscar', 'Steve')
print('Length of Tuple:', len(z))
