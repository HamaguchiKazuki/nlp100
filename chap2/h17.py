# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

import subprocess

def sort_item(fname, n):
    return sorted(list({line.split()[n-1] for line in open(fname)}))

def check_sort_item(fname, n):
    cmd = 'cut -f {} {} | LANG=C sort | uniq'.format(str(n), fname)
    return subprocess.check_output(cmd, shell=True).decode()

if __name__ == '__main__':
    fname, n = 'hightemp.txt', int(input('N--> '))
    for e in sort_item(fname, n):
        print(e)

    print('\n', '======= 確認用 =======', '\n')

    print(check_sort_item(fname, n))
