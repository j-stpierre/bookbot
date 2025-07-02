from stats import count_words, character_count, sorted_counts
import sys


def get_book_text(filepath):
    filecontents = ""
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    word_count = count_words(contents)
    char_count = character_count(contents)
    sorted = sorted_counts(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            char_name = char["char"]
            char_count = char["num"]
            print(f"{char_name}: {char_count}")
    print("============= END ===============")


main()
