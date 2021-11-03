'''

【実行結果】
> python sheep.py
何匹数えますか？： 10
羊が 1 匹
羊が 2 匹
羊が 3 匹
羊が 4 匹
羊が 5 匹
羊が 6 匹
羊が 7 匹
羊が 8 匹
羊が 9 匹
羊が 10 匹

'''

import time

a = int(input("何匹数えますか？："))
b = 1
c = 0

while True:
    c += 0.05
    time.sleep(c)
    print(f"羊が{b}匹")
    b += 1

    if b > a:
        break

    if b > 100:
        break