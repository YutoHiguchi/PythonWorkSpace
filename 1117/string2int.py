'''

【実行結果】
> python string2int.py
0
10
100

'''


def str2int(s):
    """str2int
    文字列を数値に変換した値を返す
    """

    if type(s) is str:  # 文字列かどうか確認

        # 文字列の時
        if s.isnumeric():   # 数値かどうかの確認
            return int(s)   # true

        else:
            return 0    # false

    else:
        return s    # 文字列ではなかった時

print(str2int('a'))
print(str2int('10'))
print(str2int(100))