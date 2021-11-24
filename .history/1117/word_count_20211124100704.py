'''

【実行結果】
> python word_count.py
{'from': 1, 'wikipedia': 4, 'the': 3, 'free': 2, 'encyclopedia': 3,
'this': 2, 'article': 1, 'is': 1, 'about': 2, 'for': 5, 'english': 2,
'edition': 1, 'see': 5, "wikipedia's": 2, 'home': 1, 'page': 2, 'main':
1, 'visitor': 1, 'introduction': 1, 'other': 2, 'uses': 1,
'disambiguation': 1, 'redirects': 1, 'here': 1, 'a': 1, 'list': 1, 'of':
2, 'encyclopedias': 2, 'lists': 1}

'''

import os

DATA_FILENAME = 'word_list.txt'
if os.path.isfile(DATA_FILENAME):  # ファイルが有るかの確認
    # ここからファイルを読み込む
    with open(DATA_FILENAME, 'rb') as f:  # 開いたファイルを「f」として扱う




# if os.path.isfile(DATA_FILENAME):  # ファイルが有るかの確認
#     # ここからファイルを読み込む
#     with open(DATA_FILENAME) as f:  # 開いたファイルを「f」として扱う
#         # 単語リストに格納
#         words_list = [word.strip() for word in f]
#         # strip()の時は空白文字を除去している

#     for i in range(words_list):
#         a = i.zfill(4)
#         print(f"{a}:{words_list}")
# else:  # ファイルがない時
#     words_list = []  # リストの作成