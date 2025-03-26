def counting_words(book):
    num_words = 0
    for word in book.split():
        num_words += 1
    print(f"Found {num_words} total words")
    return

def counting_letter(book):
    dict_letter = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
        'z': 0, ' ': 0, ',': 0, '.': 0, 'æ': 0,
        'â': 0, 'ê': 0, 'ë': 0, 'ô': 0
    }
    book_lower = book.lower()

    for letter in book_lower:
        for alph in dict_letter:
            if letter == alph:
                dict_letter[alph] += 1
    return dict_letter

def chars_to_sorted_list(letters):
    chars_list = []
    for char, count in letters.items():
        chars_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def cleaner(chars_list):
    for i in chars_list:
        if i["char"].isalpha():
            print(f"{i["char"]} : {i["count"]}")