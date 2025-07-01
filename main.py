from stats import word_num
from stats import char_count
from stats import dic_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book = get_book_text(sys.argv[1])

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {word_num(get_book)} total words
--------- Character Count -------""")
    for dic in dic_sort(char_count(get_book)):
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")
    
main()