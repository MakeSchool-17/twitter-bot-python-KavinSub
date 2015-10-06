import sys
# Implementation of binary heap with max-heap property
# Left child = 2 * k
# Right child = 2 * k + 1
# Parent = k / 2
class Heap:

    def __init__(self):
        self.heap = []
        self.heap.append(None)

    # Inserts the new value
    def insert(self, key, value):
        # Starts by adding a value at the end of the heap
        self.heap.append((key, value))
        k = len(self.heap) - 1
        # Percolates the value up if necessary
        parent =  int(k/2)
        #print("Values {} and {}".format(self.heap[k][0], self.heap[parent][0]))
        while parent > 0 and self.heap[parent][0] < self.heap[k][0]:
            #print("Swapping {} and {}.".format(self.heap[k][0], self.heap[parent][0]))
            self.swap(k, parent)
            k = parent
            parent = int(k/2)
    # Swaps values at the indexes provided
    def swap(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    # Returns the value at the root
    def peek(self):
        return self.heap[1]

    # Deletes the max value (The root)
    def delete_max(self):
        self.heap[1] = None
        # Compares the left and right children of the root, and does this for all levels
        k = 1
        # While heap[k] still has children
        while True:
            if self.has_right(k) and self.has_left(k): # If both children exist
                left = self.get_left(k)
                right = self.get_right(k)
                if left > right:
                    self.heap[k] = left
                    self.heap[2 * k] = None
                    k = 2 * k
                else:
                    self.heap[k] = right
                    self.heap[2 * k + 1] = None
                    k = 2 * k + 1
            elif self.has_left(k): # If a node only has one child, it only has the left child and it is on the n-1 level
                left = self.get_left(k)
                self.heap[k] = left
                self.heap[2 * k] = None
                self.heap.pop(2 * k)
                break
            elif self.has_right(k):
                right = self.get_right(k)
                self.heap[k] = right
                self.heap[2 * k + 1] = None
                self.heap.pop(2 * k + 1)
                break
            elif self.heap[k] == None:
                self.heap.pop(k)
                break

    # Helper methods return true if _child exists
    def has_right(self, k):
        return 2 * k + 1 < len(self.heap)

    def has_left(self, k):
        return 2 * k < len(self.heap)

    # Gets values from children
    def get_right(self, k):
        return self.heap[2 * k + 1]
    def get_left(self, k):
        return self.heap[2 * k]
if __name__ == '__main__':
    heap = Heap()
    heap.insert(1, "fat")
    heap.insert(2, "cold")
    heap.insert(5, "got")
    heap.insert(4, "hat")
    heap.insert(3, "mat")
    heap.insert(7, "glove")
    heap.insert(12, "gogo")
    heap.insert(1, "flat")
    print(heap.heap)
    print(heap.peek())
    heap.delete_max()
    print(heap.heap)
    print(heap.peek())
    heap.delete_max()
    print(heap.heap)
    print(heap.peek())
    heap.delete_max()
    print(heap.heap)
    print(heap.peek())
