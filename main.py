import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
from stats import word_counter, char_counter, sort_char_count

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = word_counter(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_char_count(char_counter(book_text)):
        cha = item["char"]
        num = item["num"]
        
        if not cha.isalpha():
            continue
        
        print(f"{cha}: {num}")
    print("============= END ===============")

main()