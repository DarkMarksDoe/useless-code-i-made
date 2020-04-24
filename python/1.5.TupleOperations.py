#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away


# INFO ABOUT TUPLES

# ~ Inmutable (can't add/change)
# ~ Useful for fixed data
# ~ Faster than Lists
# ~ Sequence type

#                                     CONSTRUCTORS
x = ()
x = (1, 4, 7)
x = 10, 11, 12
x = 2,  # the comma tells Python it's a tuple
print('Tupla', x, ' & type', type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print('Tupla Parse', x, ' & type', type(x))

#                                       INMUTABLE
print('\n')

x = (1, 4, 7)
# del(x[1])         # FAILS!
# x[1] = 9          # FAILS!
print(x)

y = ([1, 2], 3)     # A tuple where the 1st item is a list
del(y[0][1])        # Delete the number 2
print('Delete item from list inside Tuple', y)

y += (4,)           # Concatenating two tuples
print('Concat 2 tuples', y)