# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

str = "パタトクカシーー"

word_list = []
count = 0

for word in str:
    if count%2 == 1:
        word_list += word
    count += 1

union_word = ''.join(word_list)

print(union_word)

