'''

【実行例】
> python while_word.py
単語を入力してください： hello
単語を入力してください： world
単語を入力してください： LIST
単語リスト： ['hello', 'world']
単語を入力してください： hello
すでに登録済です
単語を入力してください： Good
単語を入力してください： bye
単語を入力してください：
終了します
これまでに覚えた単語： ['hello', 'world', 'Good', 'bye']

'''

data =[]


while True:

    a = input("単語を入力してください：")

    if a == "":
        print("終了します")
        print(f"これまでに覚えた単語：{data}")
        break

    if a == "LIST":
        print(f"単語リスト：{data}")
    elif a in data:
        print("すでに登録済みです")
    else:
        data.append(a)







