'''

【実行結果】
> python word_count_func.py
a :1
about :2
article :1
disambiguation:1
edition :1
encyclopedia :3
encyclopedias :2
english :2
for :5
free :2
from :1
here :1
home :1
introduction :1
is :18
list :1
lists :1
main :1
of :2
other :2
page :2
redirects :1
see :5
the :3
this :2
uses :1
visitor :1
wikipedia :4
wikipedia's :2

'''



DATA_FILENAME = 'sentence.txt'                 # 今回利用ファイルを指定

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

# print(new_list)