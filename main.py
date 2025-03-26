from stats import counting_words, counting_letter, chars_to_sorted_list, cleaner

def get_book_text(name):
    with open("books/" + name) as f:
        file_content = f.read()
    return file_content

def main(name):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{name}...")
    book = get_book_text(name)
    print("----------- Word Count ----------")
    counting_words(book)
    print("--------- Character Count -------")
    counting_letter(book)
    letters = counting_letter(book)
    chars_list = chars_to_sorted_list(letters)
    cleaner(chars_list)
    print("============= END ===============")
    return
    
main("frankenstein.txt")
