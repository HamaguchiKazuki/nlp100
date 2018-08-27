# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

def get_word_length(str):
    # check = [len(w)for w in [''.join([c for c in w if c.isalnum()]) for w in str.split()]]

    word_len_list = []

    for word in str.split():
        # print(word, len(word))
        alphanumeric = []
        for char in word:
            if char.isalnum():
                alphanumeric.append(char)

        union_word = ''.join(alphanumeric)
        word_len_list.append(len(union_word))

    # print(check == word_len_list)
    return word_len_list



if __name__ == '__main__':
    str = '''\
    Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.
    '''
    print(get_word_length(str))