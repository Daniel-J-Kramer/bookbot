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

def sort_on(dict):
    return dict["num"]

def get_report(path, word_count, char_dict):
    beginning_string = "--- Begin report of " + path + " ---"
    end_string = "--- End report ---"
    line_break = '\n'
    count_report = str(word_count) + " words found in the document"
    char_dict_list = []
    for c in char_dict:
        char_temp = {}
        if (c in char_dict_list) == False:
            char_temp["char"] = c
            char_temp["num"] = char_dict[c]
            if c.isalpha():
                char_dict_list.append(char_temp)
    char_dict_list.sort(reverse=True, key=sort_on)
    report = beginning_string + line_break + count_report + line_break + line_break
    string = ""
    for d in range(0, len(char_dict_list)):
        dict_temp = char_dict_list[d]
        letter = dict_temp["char"]
        number = str(dict_temp["num"])
        string = string + "The '" + letter + "' character was found " + number + " times" + line_break
    report = report + string + end_string
    return report


main()