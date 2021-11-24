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
        word = word.split(' ')

        if word in word_dic:                    # 辞書のキーに単語が存在するか？
            # if word in word_dic.keys():       #別の書き方
            word_dic[word] += 1                 # カウントアップ
        else:
            word_dic[word] = 1                  # 初めての単語なので初期値1

len_max = 0
for word in word_dic.keys():
    len_max = max(len_max, len(word))
for word in sorted(word_dic):
    print()


# print(word_dic)



def word_lower(string):
    '''文字列の中の大文字を小文字に変換し、文字列を返す'''
    return string.lower()

def delete_char(string):
    '''NG_Listの記号をスペースに置き換え、文字列を返す'''
    ng_list = '.,:()"[]'
    for c in ng_list:
        string = string.replace(c,' ')
    return string

def word_split(string):
    '''文字列をスペースで切り分け、リストを返す'''
    words = string.split(' ')
    return words

def remove_null(words_list):
    '''空のkeyの要素を削除する。辞書を返す'''
    if '' in words_list:
        del words_list['']
    if ' ' in words_list:
        del words_list[' ']
    return words_list
