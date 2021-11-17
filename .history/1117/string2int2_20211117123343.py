'''

【実行結果】
> python string2int2.py
[5, 0, 100, 10, 1]
100
0

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



def list2int(s):
    """list2int
    文字列を数値に変換した値を返す（List 対応）
    """

    if type(s) is str:  # 文字列か?

        return str2int(s)

    elif type(s) is list:   # 文字列ではなくリストかどうかの条件式
        # result = [str2int(i) for i in s]

        result = []

        for i in s:
            result.append(str2int(i))

        return result

    else:
        return None


print(list2int(['5', 'ab', '100', 10, 1]))
print(list2int('100'))
print(list2int('xyz'))
