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
    c += 0.2
    time.sleep(c)
    print(f"羊が{b}匹")
    b += 1

    if b > a:
        break

    if b > 100:
        break


# ↓先生の回答

# import time

# while True:
#     max_num = int(input("何匹数えますか？："))
#     if max_num > 100:
#         print("多すぎます")
#         continue
#     else:
#         break

# my_count = 1
# while my_count <= max_num:
#     print("羊が{}匹".format(my_count))
#     time.sleep(my_count/10)
#     my_count += 1