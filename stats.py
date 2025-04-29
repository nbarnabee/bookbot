def get_book_text(path) :
    with open(path) as file:
        contents = file.read()
        return contents

def get_word_count(string) :
    return len(string.split())