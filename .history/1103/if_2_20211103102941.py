'''

 次のプログラムを作成してください【if_2.py】
    o 適当な文字列を入力する
         空文字を入力したら終了
         そうでなければ、以下を繰り返し実行する
    o 数字のみの場合→「数字」と出力
    o アルファベットのみの場合→「アルファベット」と出力
    o アルファベットと数字の場合→「アルファベットと数字」と出力
    o 上記以外の場合→「その他」と出力


【実行例】
> python if_2.py
好きな文字を入力してください： 10
数字
好きな文字を入力してください： abc
アルファベット
好きな文字を入力してください： 10abc
アルファベットと数字
好きな文字を入力してください： ===abc
その他
好きな文字を入力してください： abc100---
その他
好きな文字を入力してください：

【参考】
>>> a = "10abc"
>>> a.isdigit()
False
>>> a.isdecimal()
False
>>> a.isalpha()
False
>>> a.isnumeric()
False
>>> a.isalnum()
True


'''


while True:
    a = input("好きな文字を入力してください：")

    if a == "":
        break

    if a.isalnum(): # アルファベットか数字か？

        if a.isnumeric():
            print("数字")

        elif a.isalpha():
            print("アルファベット")

        else:
            print("アルファベットと数字")

    else:
        print("その他")

