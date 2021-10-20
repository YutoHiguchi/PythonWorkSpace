'''
python3 list4.py
整数を入力してください： 5
1〜5 までの合計： 15
平均： 3.0

'''

n=input("整数を入力してください")
# 入力した値を整数にしないといけない num = int(n)
numbers = range(1, int(n) + 1)

total = 0
average = 0
num = int(n)
i = 0

while i <= num:
    total += i
    i += 1
average = total/num

print(f"1~{n}までの合計:{total}")
print(f"平均:{average}")