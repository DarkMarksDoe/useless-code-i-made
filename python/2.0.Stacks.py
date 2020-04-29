
#!                               COURSE DATA STRUCTURES

# *               Native Python Data Structures, Operators for Sequence
# *               Types like: Strings, List, Tuples
# ?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# * If this code works, it was written by DarkMarksDoe. If not, I don't know
# * who wrote it, just pass away

#!                                 STACKS

# TODO INFO ABOUT STACKS

# * Stack is a LIFO data structure --Last In, First Out--
# * Use append() to push an item onto the stack
# * Use pop() to remove an item

my_stack = list()
my_stack.append(1)
my_stack.append(4)
my_stack.append(7)
my_stack.append(0)
print('Stack', my_stack)

# ? Deleting items
print('1st pop', my_stack.pop())
print('2nd pop', my_stack.pop())
print('Resultant list', my_stack)


# !                        STACK USING LIST WITH WRAPPER CLASS
print('\n')

# * Creating a stack class and a full set of Stack Methods
# * But the underlying data structure is really a Python List
# * For Pop and Peek methods we first check wheter the stack is empty, to avoid exceptions

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

# * Using the Stack Wrapper Class


my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
print('Class: ', my_stack)
print('Pop 1: ', my_stack.pop())
print('Peek: ', my_stack.peek())
print('Pop 2: ', my_stack.pop())
print('Pop 3: ', my_stack.pop())
print('Pop 4: ', my_stack.pop())


