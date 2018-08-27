# "Hi He Lied Because Boron Could Not Oxidize Fluorine.
#  New Nations Might Also Sign Peace Security Clause.
# Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）
# への連想配列（辞書型もしくはマップ型）を作成せよ．


ses = 'H B C N O F P S K V Y I U'.split()
des = '''\
He Li Be Ne Na Mg Al Si Cl Ar Ca Sc Ti Cr Mn Fe Co Ni Cu Zn
Ga Ge As Se Br Kr Rb Sr Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb
Te Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf
Ta Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa Np Pu
Am Cm Bk Cf Es Fm Md No Lr
'''.split()

def element(str):
    #　文を単語に分解、辞書（連想配列）の作成
    word_list = [''.join([char for char in word if char.isalnum()]) for word in str.split()]
    word_dic = {}

    # 単語の仕分け
    for i in range(len(word_list)):
        if word_list[i][:2] in des:
            word_dic[word_list[i]] = word_list[i][:2]
        elif word_list[i][0] in ses:
            word_dic[word_list[i]] = word_list[i][0]
    return word_dic


if __name__ == '__main__':
    str = '''\
    Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause. Arthur King Can.
    '''

    print(element(str))