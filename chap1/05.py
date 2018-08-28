# 与えられたシーケンス（文字列やリストなど）から
# n-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，
# 文字bi-gramを得よ．

def str2wl(src):
    return [s.split()
            for s in src.rstrip('.').split('.')
            ]

def str2cl(src):
    return [list(w)
            for w in
            [''.join([c
                for c in w
                    if c.isalnum()])
                for w in src.split()
                      ]
            ]

def n_gram(n, gl):
    return [g[i:i+n]
            for g in
                gl
                for i in range(len(g)-n+1)
                    if len(g) >= n
            ]

if __name__ == '__main__':
    str = 'I am an NLPer'

    print(n_gram(2, str2wl(str)))
    print(n_gram(2, str2cl(str)))