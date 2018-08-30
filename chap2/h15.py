# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

import subprocess

def tail(fname, num):
    return ''.join([line for line in open(fname)][-num:])

def check_tail(fname, num):
    return subprocess.check_output(['tail', '-n', str(num), fname]).decode()

if __name__ == '__main__':
    fname = 'hightemp.txt'
    num = int(input('N--> '))
    print(tail(fname, num))

    print('\n', '======= 確認用 =======', '\n')

    print(check_tail(fname, num))