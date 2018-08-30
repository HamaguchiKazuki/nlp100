# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

#
# usage python h13.py {filename} ...
#

import sys
import subprocess

def col_get(filenames):
    alldata = [[line.rstrip()
           for line in
           open(filename)]
          for filename in filenames]
    return [[data[i]
             for data in
             alldata]
            for i in range(len(alldata[0]))]

if __name__ == '__main__':
    # fns = sys.argv[1:]
    fns = ['col1.txt', 'col2.txt'] # deback
    filename1, filename2 = 'col1.txt', 'col2.txt'

    for l in col_get(fns):
        data_list = '\t'.join([str(d) for d in l])
    with open('col3.txt', 'w') as f:
        f.writelines(data_list)

    print(subprocess.check_output(['paste', filename1, filename2]).decode())
