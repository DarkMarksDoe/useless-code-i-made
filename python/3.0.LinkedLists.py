
# !                               COURSE DATA STRUCTURES

# *               Native Python Data Structures, Operators for Sequence
# *               Types like: Strings, List, Tuples
# ?               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# * If this code works, it was written by DarkMarksDoe. If not, I don't know
# * who wrote it, just pass away

# !                                      LINKED LISTS

# TODO INFO ABOUT NODE CLASS

# * Is a constructor that sets the data passed in, and optionaly can set the *next_node* and *prev_node*
# * It also has a str method to give a string representation for printing
# * Nate that *prev_node* is only used for Doubly Linked Lists


class Node:

    def __init__(self, d, n=None, p=None):  # ? data, nextNode, previousNode
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data)+')')

# !                                  LinkedList Class

# TODO INFO ABOUT LinkedList Class

# * Is an object that has 2 attributes, a root node that defaults to None, and the F!#$@ instructor
# ? Add .- Method that recieves a piece of data, creates a new Node, setting the root at the root node and changes de LL's root ponter to the new node, and increments size
# ? FINF .- Iterates through the nodes until it finds the data passed in. If finds the data it will return it, otherwise returns None.expandtabs()
# ? Remove .- Needs ponters to this_node and prev_node. If it finds the data, it needs to check if it is in the root node (prev_node is None) before deciding how to bypass the delated node.
# ? PrintList .- Iterates the list and prints each node.


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:  # ? DATA IS NON-ROOT
                    prev_node.next_node = this_node.next_node
                else:  # ? DATA IS IN ROOT NODE
                    self.root = this_node.next_node
                self.size -= 1
                return True  # * DATA REMOVED
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False  # ! DATA NOT FOUND

    def printList(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')


# !                             LinkedList TEST CODE

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.add(17)
myList.add(21)
myList.add(28)
myList.printList()
print('Size 1: ' + str(myList.size))
myList.remove(12)
myList.printList()
print('Size 2: ' + str(myList.size))
print('Find: ', myList.find(21))
print('Root: ', myList.root)
