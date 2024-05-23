def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for i in sorted(num_letters, key = num_letters.get, reverse=True):
        if i.isalpha():
            print (f"The \'{i}\' character was found {num_letters[i]} times")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    text = text.lower()
    count_dict = {}
    for char in text:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()