# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力
#
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(str):
    # return ''.join([chr(219 - ord(c)) if 96 < ord(c) < 123 else c for c in str])
    cipher_list = []
    for char in str:
        if char.islower():
            char = chr(219 - ord(char))
        cipher_list.append(char)
    return ''.join(cipher_list)

if __name__ == '__main__':
    ecd = cipher('This is a pen.')
    dcd = cipher(ecd)

    print(ecd, dcd)
