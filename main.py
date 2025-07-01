def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_num(book):
    return len(book.split())

def main():
    total = word_num(get_book_text("books/frankenstein.txt"))
    print(f"{total} words found in the document")

main()