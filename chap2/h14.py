# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

def head(filename, number):
        with open(filename) as data_file:
            return [line.rstrip() for i, line in enumerate(data_file) if i < number]

if __name__ == '__main__':
    filename = 'hightemp.txt'
    n = int(input('N--> '))
    print('\n'.join(head(filename, n)))