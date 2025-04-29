from stats import get_book_text
from stats import get_word_count

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")

main()
