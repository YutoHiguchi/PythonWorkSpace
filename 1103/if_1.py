'''

【実行例】
> python3 if_1.py
好きな文字を入力してください： 10
数字
好きな文字を入力してください： abc
アルファベット
好きな文字を入力してください： aaa111
その他
好きな文字を入力してください： ===
その他
好きな文字を入力してください：

'''

while True:
    a = input("好きな文字を入力してください：")

    if a == "":
        break

    # if True == a.isdecimal():
    # if a.isdecimal():
    if a.isnumeric():
        print("数字")

    # else if ではなく elif ？
    elif a.isalpha():
        print("アルファベット")

    else:
        print("その他")





