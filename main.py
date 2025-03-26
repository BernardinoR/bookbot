from stats import counting_words, counting_letter, chars_to_sorted_list, cleaner
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_content = f.read()
    return file_content

def main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book = get_book_text(path_to_book)
    print("----------- Word Count ----------")
    counting_words(book)
    print("--------- Character Count -------")
    counting_letter(book)
    letters = counting_letter(book)
    chars_list = chars_to_sorted_list(letters)
    cleaner(chars_list)
    print("============= END ===============")
    return
    
main(path_to_book)
