import sys
import re
import time

# Node class
class Node:
    #data = 0
    #key = None
    #next = None

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

    #def __init__(self, data):
        #self.data = data

# Class for LinkedList
class LinkedList:
    head = None
    tail = None

    def __str__(self):
        pairs = self.get_values()
        string = "[Head -> "
        for pair in pairs:
            string += "({}, {}) -> ".format(pair[0], pair[1])
        string += "None]"
        return string
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

    # Returns a list of pairs (key, value)
    def get_values(self):
        pairs = []
        current = self.head
        while current != None:
            pairs.append((current.key, current.data))
            current = current.next
        return pairs

    # Returns True if the list is empty
    def is_empty(self):
        return self.head == None and self.tail == None

class HashTable:
    table = []

    entries = 0
    buckets = 0
    critical_point  = 0.667

    def __init__ (self, size):
        self.buckets = size
        for i in range(size):
            self.table.append(LinkedList())

    # Adds a new Key: Value pair to the hash table. Return False if unable to set
    def set(self, key, value):
        # Exit function if key already exists
        if self.contains(key) == True:
            return False
        node = Node(key, value)
        index = self.hash(key)
        self.table[index].append(node)
        self.entries += 1
        # Calculates load factor. Calls rehash if necessary
        load_factor = float(self.entries) / float(self.buckets)
        if load_factor > self.critical_point:
            self.rehash()
        return True

    # Table[key] -> Value
    def get(self, key):
        index = self.hash(key)
        linked = self.table[index]
        node = linked.find(lambda k: k == key)
        if node == None:
            return None
        return node.data
    # Gets the node itself
    def get_node(self, key):
        index = self.hash(key)
        linked = self.table[index]
        node = linked.find(lambda k: k == key)
        if node == None:
            return None
        return node
    # Updates an existing entry in the hashtable
    def update(self, key, new_val):
        index = self.hash(key)
        linked = self.table[index]
        node = linked.find(lambda k: k == key)
        if node == None:
            return "Unable to find key: {}".format(key)
        node.data = new_val

    def get_pairs(self):
        pairs = []
        for list in self.table:
            pairs += list.get_values()
        return pairs

    # Returns a key list
    def get_keys(self):
        pairs = self.get_pairs()
        keys = []
        for pair in pairs:
            keys.append(pair[0])
        return keys

    # Returns a list of values
    def get_values(self):
        pairs = self.get_pairs()
        values = []
        for pair in pairs:
            values.append(pair[1])
        return values

    # Hash function that makes use of built in hash function
    def hash(self, key):
        return hash(key) % len(self.table)

    # Helper function to print out a table
    def print_table(self):
        for index in range(len(self.table)):
            if not self.table[index].is_empty():
                sys.stdout.write("[{}]: ".format(index))
                self.table[index].print_list()
        print('\n')

    # Returns true if the table contains the provided key
    def contains(self, key):
        index = self.hash(key)
        linked_list = self.table[index]
        pairs = linked_list.get_values()
        for pair in pairs:
            if pair[0] == key:
                return True
        return False

    # Called when load factor exceeds critical value
    def rehash(self):
        new_size = self.buckets * 2
        new_table = []
        # Reset table
        self.keys = []
        self.values = []
        self.entries = 0
        self.buckets = new_size
        # Create new table
        for i in range(new_size):
            new_table.append(LinkedList())
        # Set new table
        temp_table = self.table
        self.table = new_table
        for list in temp_table:
            for pair in list.get_values():
                self.set(pair[0], pair[1])


if __name__ == '__main__':

    f = lambda data: data > 10

    table = HashTable(5)
    table.set("Apples", 5)
    table.set("Bananas", 7)
    table.set("Cherries", 13)
    table.set("Dates", 17)
    table.set("Fruits", "Vegetables")
    table.print_table()
    print(table.get_pairs())
    print(table.get_keys())
    print(table.get_values())

    #table.print_table()
    #table.update("Fruits", "Not Vegetables")
    #table.print_table()
