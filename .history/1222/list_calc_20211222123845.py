'''

【実行結果】
> python list_calc.py
calc :3
calc :+
calc :5
calc :*
calc :*
入力が正しくありません。
calc :2
calc :=
入力した計算式： 3+5*2
計算結果： 13

'''


calc = []
kigou = True    # True→次の入力は数字 False→次の入力は記号


while True:



formula = ''.join(calc)
print(f'入力した計算式：{formula}\n計算結果：{eval(formula)}')

