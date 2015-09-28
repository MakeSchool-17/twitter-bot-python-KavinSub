import sys
import word_frequency
import random
import time

true_rand = []

# Generates the list for random_word
def gen_list(histogram):
    keys = tuple(histogram.keys())

    # The list that contains every occurence of the words
    rand = []

    for word in keys:
        for i in range(histogram[word]):
            rand.append(word)

    return rand

# Returns a random word from the histogram based on the word occurence
def random_word(histogram):

    return true_rand[random.randint(0, len(true_rand) - 1)]

# Runs random_word [trials] times
def random_trials(trials, histogram):
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

    test = 0

    print("---------------RESULTS---------------")
    # Prints all the frequencies
    for word in keys:
        print("Test Frequency: {} -> {} Actual Frequency: {} -> {}".format(word, freq[word]/trials, word, histogram[word]/total))


if __name__ == '__main__':
    time_start = time.clock()
    trials = 1000000

    source_text = "text_files/" + sys.argv[1]


    histogram = word_frequency.histogram(source_text)

    true_rand = gen_list(histogram)
    random_trials(trials, histogram)

    #print("Random word: {}".format(random_word(histogram, rand)))

    print("---------------STATISTICS---------------")
    time_end = time.clock()
    time_diff = time_end - time_start
    #print("Time taken: {} seconds".format(time_diff))
    print("Time taken: %.3f seconds" % (time_diff))
    print("Memory consumed: {} Bytes".format(sys.getsizeof(true_rand)))
    print()
