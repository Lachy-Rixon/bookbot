def word_num(book):
    return len(book.split())

def char_count(book):
    char_dic = {}
    for char in book.lower():
        if char in char_dic:
            char_dic[f'{char}'] += 1
        else:
            char_dic[f'{char}'] = 1
    return char_dic

def sort_on(c):
    return c["num"]

def dic_sort(char_dic):
    char_dic_list = []
    for char in char_dic:
        if char.isalpha():
            char_dic_list.append({"char":char, "num":char_dic[char]})
    char_dic_list.sort(reverse=True, key=sort_on)
    return char_dic_list
    
