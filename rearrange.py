import sys
import random

words = sys.argv[1::]

length = len(words)
new_words = list()

i = 0
while i < length:
    new_words.append(words.pop(random.randint(0, len(words) - 1)))
    i = i + 1

for word in new_words:
    sys.stdout.write(word + " ")

print()
