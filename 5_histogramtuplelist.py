import sys
import re
import time

# Returns the index at which a word is located
def linear_search(list, word):
    for i in range(len(list)):
        if list[i][0] == word:
            return i

    return -1

# Creates the tuplelist histogram
def histogram(source_text):
    # Open file, read text
    text_file = open(source_text)
    text = text_file.read()
    text = text.lower()

    # Regular Expressions are used to strip all non alphabetic characters
    regex = re.compile('[^a-zA-Z\']')
    inter = regex.sub(' ', text)
    inter = tuple(inter.split())

    histogram = []

    for word in inter:
        index = linear_search(histogram, word)

        if index >= 0:
            histogram[index] = (word, histogram[index][1] + 1)
        else:
            histogram.append((word, 1))

    return histogram

# Returns the frequency of a word
def frequency(histogram, word):
    return histogram[linear_search(histogram, word)][1]

if __name__ == '__main__':

    time_100 = 0
    time_1000 = 0
    trials = 10000

    source_text = "text_files/" + sys.argv[1]
    word = "fish"
    if len(sys.argv) >= 3:
        word = sys.argv[2]

    histogram = histogram(source_text)
    print("Histogram created. Time is %.3f seconds." % (time.clock()))
    time_start = time.clock()
    for i in range(trials):
        if i == 99:
            time_100 = time.clock()

        frequency(histogram, word)

    time_1000 = time.clock()

    print("100 trials -> %.3f seconds\n%d trials -> %.3f seconds" % (time_100 - time_start, trials, time_1000 - time_start))
