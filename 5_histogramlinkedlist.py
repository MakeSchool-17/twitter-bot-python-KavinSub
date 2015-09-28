import sys
import re

# Node class for the linked list
class Node:
    word = ""
    frequency = 0
    next_node = None

    # Inserts a node after the current node
    def insert_next(node):
        if self.next_node == None:
            self.next_node = node
        else:
            node.next_node = self.next_node.next_node
            self.next_node = node

# Inserts a node into the list
def insert_node(head, node):

    # Finds the position of the next node
    if head == None:
        head = node
    else:
        current = head

        while node.data < current.data
