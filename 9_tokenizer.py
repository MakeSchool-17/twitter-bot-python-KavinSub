import re
import sys
import hashtable_6
import heap_10

#regex_string = '(\".+\"|[^\s]+)'
regex_string = '[^\s\";:]+'

# Parses through a source text, returns a list of tokens
def tokenizer(source_text):
    source = open(source_text)
    raw_text = source.read()
    tokens = re.findall(regex_string, raw_text)
    return tokens

# Creates a hashtable histogram using tokenizer
def hash_histogram(tokens, size):
    hashtable = hashtable_6.HashTable(size)
    for token in tokens:
        if hashtable.set(token, 1) == False:
            hashtable.update(token, hashtable.get(token) + 1)
    return hashtable

# Creates a heap histogram using a hashtable
def heap_histogram(hashtable):
    pairs = hashtable.get_pairs()
    heap = heap_10.Heap()
    for pair in pairs:
        heap.insert(pair[1], pair[0])
    return heap

if __name__ == '__main__':
    source_text = "text_files/" + sys.argv[1]

    tokens = tokenizer(source_text)
    hashtable = hash_histogram(tokens, 500)
    print(hashtable.buckets)

    heap = heap_histogram(hashtable)
    print(heap.get_top(5))
    #print(hashtable.get_pairs()[0:100])
    #print(len(hashtable.get_keys()))
