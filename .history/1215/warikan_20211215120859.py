'''

【実行結果 例 1】
支払合計金額を入力してください： 10000
参加者人数を入力してください： 3
支払金額： 3,400 円 (2 人)
幹事金額： 3,200 円
【実行結果 例 2】
支払合計金額を入力してください： 10000
参加者人数を入力してください： 6
支払金額： 1,700 円 (5 人)
幹事金額： 1,500 円

'''


import math
#no hint!


def input_int(message):
    '''messageを表示、入力値 (int) を返す。数値以外は０を返す'''

    value = input(f'{message}を入力してください：')
    if value.isnumeric():
        value = int(value)
    else:
        value = 0
    return value


def calc_payment(total, num_people):
    '''合計金額と人数から金額を計算する。戻り地は、参加者の金額と幹事の金額を[リスト]で返す'''
    pay_people = total / num_people
    pay_people = math.ceil(pay_people / 100) * 100
    pay_coodinator = total - pay_people * (num_people - 1)
    return [pay_people, pay_coodinator]

def output_payment():
    '''参加者の支払金額、幹事の支払金額'''
    '''参加人数を書式化して出力（戻り値なし）'''

# main
total = input_int('支払い合計金額')
num_people = input_int('参加者人数')