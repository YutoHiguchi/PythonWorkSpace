'''

【実行結果】
> python func_2.py
5000 の税込金額は 5500 円
5000 の消費税 8%の税込金額は 5400 円
5000 の消費税-5%の税込金額は None 円

'''

# 先生の解答


def tax_included(price, tax=10):
    '''税込金額を計算する。税率を省略した場合は10%になる'''

    # if tax < 0:   return None
    if tax < 0:
        return None
    else:
        return int(price * (1 + tax / 100))


# main
# 5000円の税込金額は5500円
print('{}の税込金額は{}円'.format(5000, tax_included(5000)))
# 5000の消費税8%の税込金額は5400円
print('{}の税込金額は{}円'.format(5000, tax_included(5000, 8)))
# 5000の消費税-5%の税込金額はNone円
print('{}の税込金額は{}円'.format(5000, tax_included(5000, -5)))


# ↓自分で書いたやつ
# def  tax_included(args):
#     taxmoney = args * 1.1
#     taxmoney_8 = args * 0.8
#     print(f'{args}の税込金額は{taxmoney}円')
#     print(f'{args}の消費税8%の税込金額は{taxmoney_8}')

# tax_included(5000)
