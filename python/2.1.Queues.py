
#!                               COURSE DATA STRUCTURES

# *               Native Python Data Structures, Operators for Sequence
# *               Types like: Strings, List, Tuples
# ?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# * If this code works, it was written by DarkMarksDoe. If not, I don't know
# * who wrote it, just pass away

#!                                      QUEUES

# TODO INFO ABOUT QUEUES

# * Stack is a FIFO data structure --First In, First Out--
# * Deque is a double-ended queue, but we can use it for our queue.
# * We use append() to enqueue and item, and popleft() to dequeue an item.pop()

from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(3)
my_queue.append(5)
print('My queue: ', my_queue)
print('My queue: ', my_queue.popleft())

# * Using the Stack Wrapper Class
print('\n')


class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size = len(self.queue)
        return item

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else:
            return None

    def get_size(self):
        return self.size

    def __str__(self):
        return str(self.queue)


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(5)
print('Class:', my_queue)
print('Dequeue:', my_queue.dequeue())
print('Size:', my_queue.get_size())
print('Dequeue:', my_queue.dequeue())
print('Size:', my_queue.get_size())
print('Enqueue:', my_queue.enqueue(9))
print('Class 2:', my_queue)
print('Size:', my_queue.get_size())
print('Dequeue:', my_queue.dequeue())
