# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

def word_pick(str1, str2):
    min_len = len(str1) if len(str1) < len(str2) else len(str2) # 単語の長さが短い方を選択
    # 内包表記したもの
    # return ''.join([str1[i]+str2[i] for i in range(min_len)]) + str1[min_len::]+str2[min_len::]
    # 分解
    word_list = []
    for i in range(min_len):
        word_list += str1[i] + str2[i]
    word_list += str1[min_len::] + str2[min_len::]

    alt_union_word =''.join(word_list)
    return alt_union_word

if __name__ == '__main__':
    print(word_pick('パトカー', 'タクシー'))
