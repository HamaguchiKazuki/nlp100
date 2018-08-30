# col1.txtとcol2.txtをマージ

#
# usage python h13.py {filename} ...
#

import sys

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
    fns = sys.argv[1:]
    # fns = ['col1.txt', 'col2.txt'] # deback
    for l in col_get(fns):
        print('\t'.join([str(d) for d in l]))