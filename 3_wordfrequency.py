import sys
import re
import time

def histogram(source_text):
    # Open file, read text
    text_file = open(source_text)
    text = text_file.read()
    text = text.lower()

    # Regular Expressions are used to strip all non alphabetic characters
    regex = re.compile('[^a-zA-Z\']')
    inter = regex.sub(' ', text)
    inter = tuple(inter.split())
    freq_dict = {}

    # Iterate through all words in the source text
    for word in inter:

        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict

# Returns the number of unique words in the dictionary
def unique_words(histogram):
    return len(histogram.keys())

# Returns the number of times a certain word appears
def frequency(histogram, word):
    return histogram[word]

if __name__ == '__main__':
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

        frequency(histogram, word)

    time_1000 = time.clock()

    print("100 trials -> %.3f seconds\n%d trials -> %.3f seconds" % (time_100 - time_start, trials, time_1000 - time_start))
