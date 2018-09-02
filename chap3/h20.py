# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

def load_article(fname, title):
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']

if __name__ == '__main__':
    fname, title = 'jawiki-country.json.gz', input('title--> ')
    print(load_article(fname, title))

