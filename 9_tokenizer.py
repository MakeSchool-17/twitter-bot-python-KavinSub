import re
import sys
import hashtable_6

#regex_string = '(\".+\"|[^\s]+)'
regex_string = '[^\s\";:]+'

# Parses through a source text, returns a list of tokens
def tokenizer(source_text):
    source = open(source_text)
    raw_text = source.read()
    tokens = re.findall(regex_string, raw_text)
    return tokens

if __name__ == '__main__':
    source_text = "text_files/" + sys.argv[1]

    tokens = tokenizer(source_text)
    hashtable = hashtable_6.HashTable(500)
    for token in tokens:
        if hashtable.set(token, 1) == False:
            hashtable.update(token, hashtable.get(token) + 1)
    #print(hashtable.get_pairs()[0:100])
    #print(len(hashtable.get_keys()))
