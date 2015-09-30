import sys
import re

regex_string = "[-()*_]"
# "^A-z0-9\',.\"/\n?!;:"
def parse(filename, new_file):
    # Get file text
    source_file = open(filename)
    source_text = source_file.read()
    source_file.close()

    # Uses regex on string
    regex = re.compile(regex_string)
    text = regex.sub(' ', source_text)

    # Write new text to new file
    new_file = open(new_file, mode = 'w')
    new_file.write(text)

if __name__ == '__main__':

    source_file = "text_files/" + sys.argv[1]
    new_file = "text_files/" + sys.argv[2]

    parse(source_file, new_file)
