import subprocess

def tab2space(fn):
    return ''.join([line.replace('\t', ' ') for line in open(fn)])

def check_tab2space(fn):
    return subprocess.check_output(['sed', '-e', 's/\t/ /g', fn]).decode()

if __name__ == '__main__':
    output = tab2space('hightemp.txt')
    check = check_tab2space('hightemp.txt')

    print(output)
    print(check)
    print(output == check)