
#!                               COURSE DATA STRUCTURES

# *               Native Python Data Structures, Operators for Sequence
# *               Types like: Strings, List, Tuples
# ?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# * If this code works, it was written by DarkMarksDoe. If not, I don't know
# * who wrote it, just pass away

#!                                 LIST COMPREHENSIONS

import random

# ? This get values in a range of 10
under_10 = [x for x in range(10)]
print('Range 10:', str(under_10))

# ? Square values in a range of 10
squares = [x**2 for x in range(10)]
print('Squares:', str(squares))

# ? Odd values in a range of 10
odd = [x for x in range(10) if x % 2 == 1]
print('Odd num:', str(odd))

# ? Multiples of 10 in a range of 10
multiplies = [x*10 for x in range(10)]
print('Multiplies:', str(multiplies))

# ? Get all numbers from a string
string = 'I love u 2, 4 all the moments.'
nums = [x for x in string if x.isnumeric()]
print('Numbers: '+''.join(nums))

# ? Get index of a list item
names = ['Cosmo', 'Wanda', 'Timmy', 'Crocker']
index = [i for i, j in enumerate(names) if j == 'Timmy']
print('Index: ', str(index[0]))

# ? Delete Item from a list item
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print('Delete: ', letters, letrs)

# ? Nested Loop iteration for 2D lists
# * b is a subset and x is the values
a = [[1, 2], [3, 4]]
newList = [x for b in a for x in b]
print('2D: ', newList)
