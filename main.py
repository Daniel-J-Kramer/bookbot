def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = countwords(text)
    char_dict = countcharacters(text)
    report = get_report(book_path, word_count, char_dict)
    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def countwords(text):
    list = text.split()
    return len(list)

def countcharacters(text):
    lowered_contents = text.lower()
    contents_dictionary = {}
    for c in lowered_contents:
        if c in contents_dictionary:
            contents_dictionary[c] += 1
        else:
            contents_dictionary[c] = 1
    return contents_dictionary

def get_report(path, word_count, char_dict):
    beginning_string = "--- Begin report of " + path + " ---"
    end_string = "--- End report ---"
    line_break = '\n'
    count_report = str(word_count) + " words found in the document"
    report = beginning_string + line_break + count_report + line_break
    
    report = report + end_string
    return report


main()