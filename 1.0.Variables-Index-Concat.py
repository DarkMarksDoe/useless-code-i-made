#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples    
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/               

#If this code works, it was written by DarkMarksDoe. If not, I don't know
#who wrote it, just pass away

#                                      STRING, LIST, TUPLES


#String variable
x = 'orange'
print("3rd character ",x[3])

#List of Strings
x = ['apple','banana', 'guava']
print("2nd item ", x[1])

#Tuple of Strings
x = ('Jhon', 'Oscar', 'Steve')
print("1st item ", x[0])

#                                             INDEXES
print('\n')

#[start : end+1 : step]
x = "computer"
#Print first character
print(x[0])
#Print second to the fourth character
print(x[1:4])
#Starts in second character, move to 7 character and move 2 steps
print(x[1:6:2])
#Starts in 4 character to end of string
print(x[3:])
#Returns the 1st character from the end
print(x[-1])
#Returns the 3rd character from the end
print(x[-3])
#return the string without the last 2 characters
print(x[:-2])

#                                             CONCATENATING
print('\n')

#String
x = 'orange' + 'juice'
print('Concat Strings: ', x)

#List
y = ['apple', 'banana'] + ['guava']
print('Concat Lists: ',y)

#Tuple
#We need to indicate with ',' fow know that is a tuple with a unique item
z = ('Jhon', 'Oscar')+('Steve',)
print('Concat Tuples: ', z)