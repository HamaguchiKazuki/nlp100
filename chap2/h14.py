# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import subprocess

def head(filename, number):
        # with open(filename) as data_file:
        #     return '\n'.join([line.rstrip() for i, line in enumerate(data_file) if i < number])
        return ''.join([line for line in open(filename)][:number])

if __name__ == '__main__':
    filename = 'hightemp.txt'
    n = int(input('N--> '))
    print((head(filename, n)))

    print('\n', '======= 確認用 =======', '\n')
    output = subprocess.check_output(['head', '-n', str(n), filename])
    print(output.decode())