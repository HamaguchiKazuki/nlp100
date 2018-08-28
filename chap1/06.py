# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def str2cl(src):
    # return [list(w) for w in [''.join([c for c in w if c.isalnum()]) for w in src.split()]]
    # 文章を分ける
    word_list = []
    for word in src.split():
        # 単語を整形する('This' 'is' 'pen.' -> 'This' 'is' 'pen')
        char_list = []
        for char in word:
            if char.isalnum():
                char_list.append(char)
        word_list.append(char_list)
    return word_list

def n_gram(n, gl):
    n_gram_list = []
    for g in gl:
        if len(g) >= n:
            for i in range(len(g)-n+1):
                n_gram_list.append(g[i:i+n])
    return n_gram_list

if __name__ == '__main__':
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X = set(map(''.join, n_gram(2, str2cl(s1))))
    Y = set(map(''.join, n_gram(2, str2cl(s2))))

    # sets
    print('X =', X)
    print('Y =', Y)

    # sum, product, diff
    print('X + Y =', X.union(Y))
    print('X * Y =', X.intersection(Y))
    print('X - Y =', X.difference(Y))

    # include 'se' or not
    print('X include "se":', 'se' in X)
    print('Y include "se":', 'se' in Y)


