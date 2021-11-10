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

#課題3

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

    input_word = input("単語を入力してください：") #input_wordに入力値格納

    if input_word == "": #入力値が"""(空)だった場合
        break # breakで抜ける

    if input_word == "LIST":    #LISTと入力された時の処理
        print(f"単語リスト：{words_list}")  #単語が入っているリストを出力
        continue    #continueで続ける

    if input_word in words_list:    #入力された値がリストに存在している場合
        print("すでに登録済みです")
        continue    #continueで続ける

    else:   #入力された値がリストに存在していない場合
        words_list.append(input_word)   #入力値をリスト(words_list)に繋げている

#終了時のメッセージ
print("終了します")
print(f"これまでに覚えた単語：{words_list}")
f = open('test.txt', 'w')



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

