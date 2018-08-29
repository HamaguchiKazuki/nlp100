# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import subprocess

def line_count(filename):
    output = subprocess.check_output(['wc', '-l', filename])
    return output.decode('utf-8')

if __name__ == '__main__':
    print(line_count('hightemp.txt'))
