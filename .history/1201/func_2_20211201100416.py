'''

【実行結果】
> python func_2.py
5000 の税込金額は 5500 円
5000 の消費税 8%の税込金額は 5400 円
5000 の消費税-5%の税込金額は None 円

'''


def tax(args):
    taxmoney = args * 1.1
    print(f'{args}の税込金額は{taxmoney}円')

tax(5000)