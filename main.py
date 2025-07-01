from stats import word_num
from stats import char_count
from stats import dic_sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    get_book = get_book_text("books/frankenstein.txt")

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found {word_num(get_book)} total words
--------- Character Count -------""")
    for dic in dic_sort(char_count(get_book)):
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")
    
main()