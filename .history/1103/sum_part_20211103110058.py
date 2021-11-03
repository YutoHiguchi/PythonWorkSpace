'''

【実行例】
> python sum_part.py
数字 1： 3 【<-数字を入力】
数字 2： 6 【<-数字を入力】
3 から 6 までの合計は 18 です

'''

a = int(input("数字1："))
b = int(input("数字2："))
i = 0

for i in range(a, b):
     i += 1

print(f"{a}から{b}までの合計：{i}")
