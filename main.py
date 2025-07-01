from stats import word_num
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    total = word_num(get_book_text("books/frankenstein.txt"))
    print(f"{total} words found in the document")
    print(char_count(get_book_text("books/frankenstein.txt")))

main()