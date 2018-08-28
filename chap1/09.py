# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば
# "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# ）
# を与え，その実行結果を確認せよ．
import random

def typoglycemia(str):
    random_sorted_list = []
    for word in str.split():
        if len(word) > 4:
            random_word = ''.join(random.sample(word[1:len(word)-1], len(word)-2))
            sorted_string = word[0]+random_word+word[len(word)-1:len(word)]
            random_sorted_list.append(sorted_string)
        else:
            random_sorted_list.append(word)
    return random_sorted_list

if __name__ == '__main__':
    str = """\
    I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .
    """
    print(typoglycemia(str))