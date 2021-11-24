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

DATA_FILENAME = 'word_list.txt'                 # 今回利用ファイルを指定

word_dic = {}                                   # 空の辞書を作成
with open(DATA_FILENAME) as f:
    # word_dic = {}                             #ここに書いてもいい
    for word in f:
        word = word.strip()                     # 改行コードを取り除く
        if word in word_dic:                    # 辞書のキーに単語が存在するか？
            # if word in word_dic.keys():       #別の書き方
            word_dic[word] += 1                 # カウントアップ
        else:
            word_dic[word] = 1                  # 初めての単語なので初期値1

# 練習4  アルファベット昇順の並び替え    sorted()--

# 最大文字数を調べる
#len_max = 0
# for word in word_dic.keys():
#   len_max = max(len_max,len(word))
# sort後 並び替え 出力処理
# for word in sorted(word_dic):
# for word in sorted(word_dic,keys()):
#   print(f'{word:{len_max}}:{word_dic[word]}')


for word in sorted(word_dic):
    # for word in sorted(word_dic.keys()):
    print(f'{word:}:{word_dic[word]}')

# print(new_list)
