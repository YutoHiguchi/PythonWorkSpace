'''

【実行例】
> python linenum.py
0001:help
0002:test
0003:Good

'''


import os

DATA_FILENAME = 'word.txt'

if os.path.isfile(DATA_FILENAME):  # ファイルが有るかの確認
    # ここからファイルを読み込む
    with open(DATA_FILENAME) as f:  # 開いたファイルを「f」として扱う
        # 単語リストに格納
        words_list = [word.strip() for word in f]
        # strip()の時は空白文字を除去している

    for i in range(words_list):
        a = i.zfill(4)
        print(f"{a}:{words_list}")
else:  # ファイルがない時
    words_list = []  # リストの作成

