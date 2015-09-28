import sys
import random
import time

# Start time
time_start = time.clock()

# Get number of words
num_words = 0
try:
    num_words = int(sys.argv[1])
except IndexError:
    print("Please enter a number.")
    sys.exit()

# Directory of file to be used
directory = "/usr/share/dict/words"

time_2 = time.clock()
# Opening the file, and creating a tuple containing all words
file = open(directory)
dictionary = tuple(file.read().split())

time_3 = time.clock()
# Print random words
for i in range(num_words):
    index = random.randint(0, len(dictionary) - 1)
    sys.stdout.write(dictionary[index])
    if i < num_words - 1:
        sys.stdout.write(" ")
print(".")

# End time
time_end = time.clock()
time_elapsed = time_end - time_start
time_create = time_3 - time_2
time_print = time_end - time_3

print("Time Total: {}\nTime Create: {}".format(time_elapsed, time_create))
