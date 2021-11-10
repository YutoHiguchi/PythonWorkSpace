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

import os

DATA_FILENAME = 'word.txt'

if os.path.isfile(DATA_FILENAME): #ファイルが有るかの確認
    #ここからファイルを読み込む
    with open(DATA_FILENAME) as f:  #開いたファイルを「f」として扱う
        #単語リストに格納
        words_list = [word.strip() for word in f]
        # strip()の時は空白文字を除去している
else:   #ファイルがない時
    words_list = [] #リストの作成

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

# ↓課題2
# data =[]

# while True:

#     a = input("単語を入力してください：")

#     if a == "":
#         print("終了します")
#         print(f"これまでに覚えた単語：{data}")
#         break

#     if a == "LIST":
#         print(f"単語リスト：{data}")
#     elif a in data:
#         print("すでに登録済みです")
#     else:
#         data.append(a)





# ↓先生の回答

# data =[]


# while True:

#     a = input("単語を入力してください：")

#     if a == "":
#         break

#     if a == "LIST":
#         print("単語リスト：",data)
#         continue

#     if a in data:
#         print("すでに登録済みです")
#         continue

#     else:
#         data.append(a)
# else:

#     pass #何もしない

# print("終了します")
# print(f"これまでに覚えた単語：{data}")

