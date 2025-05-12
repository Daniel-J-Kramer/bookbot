def count_words(contents):
    content_list = contents.split()
    word_count = len(content_list)
    return word_count

def count_characters(contents):
    lower_contents = contents.lower()
    character_count_dictionary = {}
    for c in lower_contents:
        character_count = 0
        if (c in character_count_dictionary) == False:
            for d in lower_contents:
                if c == d:
                    character_count += 1
                character_count_dictionary[c] = character_count

    return character_count_dictionary

def sort_chars(char_dictionary):
    sorted_list = []
    for c in char_dictionary:
        new_dictionary = {}
        char = c
        num = char_dictionary[c]
        new_dictionary["char"] = char
        new_dictionary["num"] = num
        sorted_list.append(new_dictionary)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]