# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

import collections, subprocess

def sort_by_frequency(fname, n):
    count_data = collections.Counter(line.split()[n-1] for line in open(fname))
    return [(key,value) for key, value in count_data.most_common()]

def check_sort_by_frequency(fname, n):
    cmd = 'cut -f {} {} | sort | uniq -c | sort -r'.format(str(n), fname)
    return subprocess.check_output(cmd, shell=True).decode()

if __name__ == '__main__':
    fname, n = 'hightemp.txt', int(input('N--> '))
    for result in sort_by_frequency(fname, n):
        print('{key} : {value}'.format(key=result[0], value=result[1]))

    print('\n', '======= 確認用 =======', '\n')

    print(check_sort_by_frequency(fname, n))


