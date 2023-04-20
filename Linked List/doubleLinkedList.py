import random


# initializes values for a data object as well as values next to it.
class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


# creates the doubly linked list
class gamesLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # iterates over the first five elements in the linked list and prints them
    def first_five(self):
        count = 0
        curr_node = self.head
        while curr_node != None and count != 5:
            print(curr_node.data)
            count += 1
            curr_node = curr_node.next_node

    # iterates over each value in the linked list until it finds the value
    # associated with the randomly generated key "Name" in the dictionaries within the linked list
    def linear_search(self, name):
        curr_node = self.head
        while curr_node != None:
            if curr_node.data['Name'] == name:
                return curr_node.data
            curr_node = curr_node.next_node

    # iterates over each item and adds 1 to a counter
    def size(self):
        count = 0
        curr_node = self.head
        while curr_node != None:
            count += 1
            curr_node = curr_node.next_node
        return count

    # inserts each line from the csv file at the end of the linked list in
    # order to maintain the order it is currently in
    def insert_end(self, data):
        new_node = Node(data)
        new_node.next_node = None
        if self.head == None:
            new_node.prev_node = None
            self.head = new_node
            return
        first_node = self.head
        while first_node.next_node:
            first_node = first_node.next_node
        first_node.next_node = new_node
        new_node.prev_node = first_node

    # determines probablity for each node being selected as 1/size of list
    # also calculates probalility of previous nodes NOT being chosen to ensure
    # equal probability throughout.
    def random(self):
        result = self.head.data
        current = self.head
        size = 2
        while current != None:
            # changes the result with probability 1/size of list
            if random.randrange(size) == 0:
                result = current.data
            current = current.next_node
            size += 1
        return result
