def get_book_text(path) :
    with open(path) as file:
        contents = file.read()
        return contents

def get_word_count(string) :
    return len(string.split())

def get_character_count(string):
    character_dict = {}
    for c in string:
        character = c.lower()
        if character_dict.get(character):
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def make_sorted_list(character_dict):
    character_list = []
    for key, value in character_dict.items():
        if key.isalpha():
            character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(dict):
    return dict["num"]

def pretty_print_list(list):
    for item in list:
        print(f"{item['char']}: {item['num']}")
