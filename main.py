import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_character_count
from stats import make_sorted_list
from stats import pretty_print_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_word_count(text)
        character_count = get_character_count(text)
        character_list = make_sorted_list(character_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        pretty_print_list(character_list)

main()
