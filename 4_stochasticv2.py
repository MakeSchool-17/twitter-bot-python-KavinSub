import sys
import word_frequency
import random
import time

types = ()
ranges = []

# sets the tuple of word types
def set_types(histogram):
    return tuple(histogram.keys())

# sets the list of range tuples
def set_ranges(histogram, types):

    index = 0
    ranges = []
    for i in range(len(types)):
        temp = histogram[types[i]]
        ranges.append((index, index + temp - 1))
        index += temp

    return ranges

# returns a random word
def random_word(histogram):
    total = sum(histogram.values())
    num = random.randint(0, total - 1)

    # Iterates through the list of ranges until a <= num <= b
    for i in range(len(types)):
        if num >= ranges[i][0] and num <= ranges[i][1]:
            return types[i]

def random_trials(histogram, trials):
    # A copy of the dictionary to store relative frequencies
    freq = histogram.copy()

    keys = tuple(freq.keys())

    # Sets all values to zero
    for word in keys:
        freq[word] = 0

    # Run random_word [trials] times
    for i in range(trials):
        freq[random_word(histogram)] += 1

    # The total number of words
    total = sum(histogram.values())

    print("---------------RESULTS---------------")
    # Prints all the frequencies
    for word in keys:
        print("Test Frequency: {} -> {} Actual Frequency: {} -> {}".format(word, freq[word]/trials, word, histogram[word]/total))



if __name__ == '__main__':

    time_start = time.clock()

    source_text = "text_files/" + sys.argv[1]

    histogram = word_frequency.histogram(source_text)

    types = set_types(histogram)
    ranges = set_ranges(histogram, types)

    random_trials(histogram, 1000)

    time_end = time.clock()
    time_diff = time_end - time_start
    print("---------------STATISTICS---------------")
    print("Time taken: %.3f seconds" % (time_diff))
    print("Memory consumed: types list -> %d, ranges list -> %d" % (sys.getsizeof(types), sys.getsizeof(ranges)))
