# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ
# 同様の処理をsplitコマンドで実現せよ．

# N = 6 division

def n_split(fname, n):
    split_line = open(fname).read().split('\n')
    lines_num = len(split_line) // n
    return [split_line[i*lines_num:(i+1)*lines_num] if i<n-1 else split_line[i*lines_num:] for i in range(n)]

if __name__ == '__main__':
    fname = 'hightemp.txt'
    n = int(input('N--> '))
    division = n_split(fname, n)
    for i in range(n):
        with open('div{:02d}.txt'.format(i), 'w') as output_file:
            output_file.writelines('\n'.join(division[i]))

