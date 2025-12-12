from stats import word_counter, char_counter

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def main():
    frank = get_book_text("books/frankenstein.txt")
    print(f"Found {word_counter(frank)} total words")
    print(char_counter(frank))

main()