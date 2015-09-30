import sys
import re
import time

# Node class
class Node:
    data = 0
    key = None
    next = None

    def __init__(self, key, data):
        self.key = key
        self.data = data

    #def __init__(self, data):
        #self.data = data

# Class for LinkedList
class LinkedList:
    head = None
    tail = None

    # Adds a node to the end of a list
    def append(self, node):

        # If list is empty
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Returns a value based on the lambda expression passed in
    def find(self, func):
        current = self.head
        while current != None:
            if func(current.key) == True:
                return current
            else:
                current = current.next

        return None

    # Data to be deleted
    def delete(self, data):
        current = self.head
        prev = None
        while current != None:

            if current.data == data:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = current.next
            prev = current
            current = current.next

    # Helper method to print a list
    def print_list(self):
        current = self.head
        while current != None:
            if current.next != None:
                sys.stdout.write("{}: {} -> ".format(current.key, current.data))
            else:
                print("{}: {}".format(current.key, current.data))
            current = current.next

    # Returns True if the list is empty
    def is_empty(self):
        return self.head == None and self.tail == None

class HashTable:
    keys = []
    values = []
    table = []

    def __init__ (self, size):
        for i in range(size):
            self.table.append(LinkedList())

    # Adds a new Key: Value pair to the hash table
    def set(self, key, value):
        node = Node(key, value)
        index = self.hash(key)
        self.table[index].append(node)
        self.keys.append(key)
        self.values.append(value)

    # Table[key] -> Value
    def get(self, key):
        index = self.hash(key)
        linked = self.table[index]
        node = linked.find(lambda k: k == key)
        if node == None:
            return "Unable to find key: {}".format(key)
        return node.data

    # Updates an existing entry in the hashtable
    def update(self, key, new_val):
        index = self.hash(key)
        linked = self.table[index]
        node = linked.find(lambda k: k == key)
        if node == None:
            return "Unable to find key: {}".format(key)
        node.data = new_val

    # Returns a key list
    def get_keys(self):
        return self.keys

    # Returns a list of values
    def get_values(self):
        return self.values

    # Hash function that makes use of built in hash function
    def hash(self, key):
        return hash(key) % len(self.table)

    # Helper function to print out a table
    def print_table(self):
        for index in range(len(self.table)):
            if not self.table[index].is_empty():
                sys.stdout.write("[{}]: ".format(index))
                self.table[index].print_list()

        print()


if __name__ == '__main__':

    f = lambda data: data > 10

    table = HashTable(50)
    table.set("Apples", 5)
    table.set("Bananas", 7)
    table.set("Cherries", 13)
    table.set("Dates", 17)
    table.set("Fruits", "Vegetables")

    print(table.get_keys())
    print(table.get_values())
    table.print_table()
    table.update("Fruits", "Not Vegetables")
    table.print_table()
