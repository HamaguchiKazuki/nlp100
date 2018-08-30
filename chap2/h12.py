# 1列目をcol1.txtに，2列目をcol2.txtに保存
import sys
import subprocess

def cut_col(filename, colnum):
    return [line.split()[colnum-1] for line in open(filename)]

if __name__ == '__main__':
    filename, colnum = sys.argv[1], int(sys.argv[2])
    # filename, colnum = 'hightemp.txt', 1 # deback

    data_list = [data+'\n' for data in cut_col(filename, colnum)]
    with open('col{}.txt'.format(colnum), 'w') as f:
        f.writelines(data_list)