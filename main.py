
import sys
from stats import count_words, count_characters, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    contents = get_book_text(path)
    word_count = count_words(contents)
    character_count = sort_chars(count_characters(contents))
    print(f"============ BOOKBOT ============\n\
Analyzing book found at {path}...\n\
----------- Word Count ----------\n\
Found {word_count} total words\n\
--------- Character Count -------\n\
{print_sortedchars(character_count)}\
============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_sortedchars(character_count):
    final_string = ""
    for d in character_count:
        if d["char"].isalpha():
            final_string += f"{d["char"]}: {str(d["num"])}\n"
    return final_string

main()