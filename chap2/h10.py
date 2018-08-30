# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import subprocess
import sys

def check_line_count(filename):
    return subprocess.check_output(['wc', '-l', filename]).decode()

def line_count(filename):
    return len([line for line in open(filename)])

if __name__ == '__main__':
    check = check_line_count('hightemp.txt')
    output = line_count('hightemp.txt')

    print(check)
    print(output)

