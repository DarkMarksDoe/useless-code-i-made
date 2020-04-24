#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away

#                             CONSTRUCTORS / COMPREHENSION
x = list()
y = ['z', 21, 'Mark', 3.1416]
tuple1 = (99, 15)
z = list(tuple1)

# List Comprehension
a = [m for m in range(8)]
print('List 0 from 8:', a)
b = [i**2 for i in range(10) if i > 4]
print('Print square numbers when i > 4:', b)

#                                        DELETE
print('\n')
# Delete a list or an item

x = [3, 7, 9, 1, 5]
# Delete 2nd character
del(x[1])
print('Delete', x)
# Delete entire list
del(x)

#                                        APEND
print('\n')
# Apend an item to a list

x = [3, 7, 9, 1, 5]
# End of the list
x.append(10)
print('Append', x)

#                                        EXTEND
print('\n')
# Append a sequence toa list

x = [3, 7, 9, 1, 5]
y = [13, 15, 17]
x.extend(y)
print('Extend', x)

#                                        INSERT
print('\n')
# Insert an item at a given index

x = [3, 7, 9, 1, 5]
x.insert(0, 0)
print('Atend 1', x)
x.insert(1, ['m', 'a'])
print('Atend 2', x)

#                                        POP
print('\n')
# Last item

x = [3, 7, 9, 1, 5]
x.pop()
print('Pop 1', x)
print('Pop Item:', x.pop())

#                                        REMOVE
print('\n')
# Remove instance of the first item

x = [3, 1, 9, 1, 3]
x.remove(1)
print('Remove', x)

#                                        REVERSE
print('\n')
# Reverse the order of the list. It is an in-place sort, meaning it changes the original list.

x = [3, 7, 9, 1, 5]
x.reverse()
print('Reverse', x)

#                                         SORT
print('\n')
# Sorted(x) returns a new sorted list without changing the original
# x.sort() puts the items of x in sorted order.

x = [3, 7, 9, 1, 5]
x.sort()
print('Sort', x)

#                                         REVERSE SORT
print('\n')
# The same that sort but, reverse JAJAJAJAJA xD

x = [3, 7, 9, 1, 5]
x.sort(reverse=True)
print('Reverse Sort', x)
