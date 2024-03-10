def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    letter_count = number_of_letters(text)
    sorted_letter_count = convert_to_list(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for letter, count in sorted_letter_count:
        print(f"The '{letter}' character was found {count} times")

    print(f"--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    return len(text.split())

def number_of_letters(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def convert_to_list(number_of_letters):
    return sorted(number_of_letters.items(), key=lambda item: item[1], reverse=True)

if __name__ == '__main__':
    main()