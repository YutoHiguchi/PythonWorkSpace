'''

【実行結果】
> python string2int2.py
[5, 0, 100, 10, 1]
100
0

'''



def list2int(s):
    """list2int
    文字列を数値に変換した値を返す（List 対応）
    """

    if type(s) is str:  # 文字列かどうか確認
        return str2int(s)

    elif type(s) is list:
        # result = [str2int(i) for i in s]

        result = []
        for i in s:
            result.append(str2int(i))
        return result

    else:
        return None



print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))


