# get num words in file
def count_words(file):
    words = file.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


# Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any uppercase letters to lowercase letters, we don't want duplicates.
def get_chars_dict(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


# sort the counts of each character in descending order
def sort_chars_dict(char_count):
    return dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))


def sort_on(dict):
    return dict["count"]


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"-- Begin report of {path} --")
    print(f"{num_words} found in the document")
    print()
    char_count = get_chars_dict(text)
    char_dict_sorted = sort_chars_dict(char_count)

    for char, count in char_dict_sorted.items():
        if char.isalpha():
            print(f"{char} appears {count} times in document")
    print("-- End report --")


main()
