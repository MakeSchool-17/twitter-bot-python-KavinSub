import sys
import re
import time

# Class for the binary tree node
class Node:
    word = ""
    freq = 0
    left = None
    right = None

    def __init__(self, word):
        self.word = word
        self.freq = 1

# Class for the binary search tree
class BinaryTree:
    head = None

    # Performs a depth first pre order traversal on the tree, and prints elements
    def in_order(self, root):
        if root == None:
            return

        self.in_order(root.left)

        print(root.word + " " + str(root.freq))

        self.in_order(root.right)

    # Inserts a node into the tree. If word already present, increase the frequency
    def insert_node(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            list = ["", ""]
            while current != None:
                parent = current
                left_child = False
                right_child = False

                if node.word == current.word:
                    current.freq += 1
                    break

                list[0] = current.word
                list[1] = node.word

                list.sort()

                if list[0] == node.word:
                    current = current.left
                    left_child = True
                else:
                    current = current.right
                    right_child = True

                if current == None:
                    if left_child == True:
                        parent.left = node
                    elif right_child == True:
                        parent.right = node

    def frequency(self, word):
        current = self.head

        while current != None:
            if current.word == word:
                return current.freq
            else:
                list = ["", ""]
                list[0] = current.word
                list[1] = word

                list.sort()

                if list[0] == word:
                    current = current.left
                else:
                    current = current.right

        return -1

# Creates the binary tree histogram
def histogram(source_text):
    # Open file, read text
    text_file = open(source_text)
    text = text_file.read()
    text = text.lower()

    # Regular Expressions are used to strip all non alphabetic characters
    regex = re.compile('[^a-zA-Z\']')
    inter = regex.sub(' ', text)
    inter = tuple(inter.split())
    histogram = BinaryTree()

    for word in inter:
        #print(word)
        histogram.insert_node(Node(word))

    return histogram


if __name__ == "__main__":


    time_100 = 0
    time_1000 = 0
    trials = 10000

    source_text = "text_files/" + sys.argv[1]
    word = "fish"
    if len(sys.argv) >= 3:
        word = sys.argv[2]

    histogram = histogram(source_text)
    
    time_start = time.clock()
    for i in range(trials):
        if i == 99:
            time_100 = time.clock()

        histogram.frequency(word)

    time_1000 = time.clock()

    print("100 trials -> %.3f seconds\n%d trials -> %.3f seconds" % (time_100 - time_start, trials, time_1000 - time_start))
