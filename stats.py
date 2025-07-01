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
