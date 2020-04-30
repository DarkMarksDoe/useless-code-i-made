
# !                               COURSE DATA STRUCTURES

# *               Native Python Data Structures, Operators for Sequence
# *               Types like: Strings, List, Tuples
# ?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# * If this code works, it was written by DarkMarksDoe. If not, I don't know
# * who wrote it, just pass away

# !                                      MAX HEAP

# TODO INFO ABOUT MAX HEAP

# * Wlays bubbles the highest value to the top, so it can be removed instantly.
# * Public functions: push(), peek(), pop()
# * Private functions: swap(), __floatUp, __bubbleDown, __str


class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > left and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


# !                         MaxHEAP TEST CODE
m = MaxHeap([100, 19, 36])
m.push(17)
print('MaxHeap:', m)
print('Pop:', m.pop())
print('Peek:', m.peek())

# ! INFO ABOUT THIS SHIT

# ? inserting an item takes O(log n)time
# ? getting the Max item takes O(1)time
# ? Removing the Max item takes O(log n)time

# * Max Heap will have 7functions
# * 1)push--adding an item to the Max Heap
# * 2)pop--removing an item from the Max Heap
# * 3)peek--take a look at what is the max number in the Max Heap
# * 4) __swap--swaps 2items
# * 5)__floatup--moves an item up through the Max Heap
# * until it is smaller than its parent
# * 6)__bubbledown--moves an item down the Max Heap
# * until it reaches its proper position
# * 7)__str__--print out the Max Heap as a list item
