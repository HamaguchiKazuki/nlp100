# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ
# （この問題はコマンドで実行した時の結果と合わなくてもよい）．

import subprocess

def sort_by_item(fname, n):
    lines = [line.split() for line in open(fname)]
    lines.sort(key=lambda line: float(line[n-1]), reverse=True)
    return lines

def check_sort_by_item(fname, n):
    cmd = 'cut -f {} {} | sort -r'.format(str(n), fname)
    return subprocess.check_output(cmd, shell=True).decode()


if __name__ == '__main__':
    fname, n = 'hightemp.txt', int(input('N-->'))
    for line in sort_by_item(fname, n):
        print('\t'.join(line))

    print('\n', '======= 確認用 =======', '\n')

    print(check_sort_by_item(fname, n))