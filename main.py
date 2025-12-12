from stats import word_counter, char_counter, sort_char_count

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def main():
    frank = get_book_text("books/frankenstein.txt")
    word_count = word_counter(frank)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_char_count(char_counter(frank)):
        cha = item["char"]
        num = item["num"]
        
        if not cha.isalpha():
            continue
        
        print(f"{cha}: {num}")
    print("============= END ===============")

main()