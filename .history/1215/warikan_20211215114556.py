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

def input_int():
    money_sum = int(input("支払金額を入力して下さい："))
    human_sum = int(input("参加者人数を入力して下さい："))


print(f"支払金額：{money_sum}")
print(f"幹事金額：{human_sum}")