'''
python3 list4.py
整数を入力してください： 5
1〜5 までの合計： 15
平均： 3.0

'''

n=input("整数を入力してください")
# 入力した値を整数にしないといけない num = int(n)
numbers = range(1, int(n) + 1)

sum(numbers)
print("1~" + n + "までの合計:" + numbers)

avg(numbers)
print("平均:" + numbers)