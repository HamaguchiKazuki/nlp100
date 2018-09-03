# 記事中に含まれるセクション名とそのレベル
# （例えば"== セクション名 =="なら1）を表示せよ．

import re
from chap3.h20 import load_article

def get_section_structure(text):
    p = re.compile('(=+)(.*?)=+')
    return [[str(m.group(2)).strip(), len(m.group(1)) - 1]
            for m in
            [p.match(line) for line in
             text.splitlines()]
            if m]


if __name__ == '__main__':
    fname, title = 'jawiki-country.json.gz', input('title--> ')
    article = load_article(fname, title)
    for section in get_section_structure(article):
        print(section[0], section[1])
