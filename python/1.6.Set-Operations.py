#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away


# INFO ABOUT SETS

# ~ Store non-duplicate items
# ~ Very fast access vs Lists
# ~ Math Set ops (union,intersect,etc)
# ~ Sets are Unordered

#                                     CONSTRUCTORS

x = {3, 5, 7, 3, 5, 3, 5, 7}
print('Set', x)

y = set()
print('Empty Set', y)

list1 = [2, 3, 4]
z = set(list1)
print('Set Parse', z)

#                                     SET OPERATIONS
print('\nSet Operations')

x = {3, 8, 5}
print('Set:', x)
x.add(7)
print('Set.add:', x)

x.remove(3)
print('Set.remove:', x)

# Get Length of Set x
print('Length Set:', len(x))

# Membership in x

print('Membership Set:', 5 in x)

# Pop random item from Set x
print('Pop Random Item Set:', x.pop(), x)

# Delete all items from Set x
x.clear()
print('Set.clear:', x)
