'''
python3 list4.py
整数を入力してください： 5
1〜5 までの合計： 15
平均： 3.0

'''

n=input("整数を入力してください")
for i in range(n):
    i += i

print("1~" + n + "までの合計:" + i)