import sys

sentence = []

sentence = sys.argv[1::]

# Checks that a sentence has been entered
if len(sentence) == 0:
    print('Enter a sentence.')
    sys.exit()

reversed_sentence = sentence[::-1]
for word in reversed_sentence:
    sys.stdout.write("{} ".format(word))

print()
