import re
from chap3.h20 import load_article

def get_category_names(text):
    p = re.compile("\[\[Category:(.*?)(\|.*\]\]|\]\])")
    return [m.group(1) for m in [p.match(l) for l in text.splitlines()] if m != None]

if __name__ == '__main__':
    fname, title = 'jawiki-country.json.gz', 'イギリス'
    article = load_article(fname, title)
    for l in get_category_names(article):
        print(l)