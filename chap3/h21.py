# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
from chap3.h20 import load_article

def get_category_lines(text):
    p = re.compile('\[\[Category:')
    return [line for line in text.splitlines() if p.match(line)]


if __name__ == '__main__':
    fname, title = 'jawiki-country.json.gz', input('title--> ')
    article = load_article(fname, title)
    for line in get_category_lines(article):
        print(line)