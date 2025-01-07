def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_character_counts(text)
    print_report(book_path, num_words, char_counts)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_counts(text):
    char_count_dict = {}
    char_counts = []

    def sort_on(dict):
        return dict["count"]

    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count_dict:
            char_count_dict[lowered_char] += 1
        else:
            char_count_dict[lowered_char] = 1

    for char_key in char_count_dict:
        if char_key.isalpha():
            char_counts.append({"char": char_key, "count": char_count_dict[char_key]})

    char_counts.sort(reverse=True, key=sort_on)

    return char_counts

def print_report(book_path, num_words, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(f"\n")
    for char_info in char_counts:
        character = char_info["char"]
        count = char_info["count"]
        print(f"The '{character}' character was found {count} times")

    print("--- End Report ---")

main()
