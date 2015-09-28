import sys

word = ""
try:
    word = str(sys.argv[1])
except TypeError:
    print("Enter a word.")
    sys.exit()

reversed_word = word[::-1]
print(reversed_word)
