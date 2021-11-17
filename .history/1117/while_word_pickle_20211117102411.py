'''

【実行例】初回
> python while_word.py
単語を入力してください： LIST
単語リスト： []
単語を入力してください： help
単語を入力してください： test
単語を入力してください： LIST
単語リスト： ['help', 'test']
単語を入力してください：
終了します
これまでに覚えた単語： ['help', 'test']
【実行例】2 回目以降
> python while_word.py
単語を入力してください： LIST
単語リスト： ['help', 'test']
単語を入力してください： Good
単語を入力してください：
終了します
これまでに覚えた単語： ['help', 'test', 'Good']

'''


import os
import pickle


DATA_FILENAME = 'word.pkl'

if os.path.isfile(DATA_FILENAME):  # ファイルが有るかの確認
    # ここからファイルを読み込む
    with open(DATA_FILENAME, 'rb') as f:  # 開いたファイルを「f」として扱う
        # 単語リストに格納
        words_list = pickle.load(f)
        # words_list = [word.strip() for word in f]

        # strip()の時は空白文字を除去している
else:  # ファイルがない時
    words_list = []  # リストの作成

while True:

    input_word = input("単語を入力してください：")  # input_wordに入力値格納

    if input_word == "":  # 入力値が"""(空)だった場合
        break  # breakで抜ける

    if input_word == "LIST":  # LISTと入力された時の処理
        print(f"単語リスト：{words_list}")  # 単語が入っているリストを出力
        continue  # continueで続ける

    if input_word in words_list:  # 入力された値がリストに存在している場合
        print("すでに登録済みです")
        continue  # continueで続ける

    else:  # 入力された値がリストに存在していない場合
        pickle.dump(input_word)
        # words_list.append(input_word)  # 入力値をリスト(words_list)に繋げている

# 終了時のメッセージ
print("終了します")
print(f"これまでに覚えた単語：{words_list}")

# ファイルに単語リストを書き込む
with open(DATA_FILENAME, 'wb') as f:  # モード：wとは
    for word in words_list:
        f.write(f'{word}\n')












