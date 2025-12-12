def get_book_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def main():
    frank = get_book_text("books/frankenstein.txt")
    print(f"Found {word_counter(frank)} total words")

main()