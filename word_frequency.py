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
    freq_dict = histogram("text_files/MobyDick.txt")
    for key in freq_dict.keys():
        print("{} {}".format(key, freq_dict[key]))
