'''

【test.csv】
氏名,国語,算数,理科,社会
A,50,80,90,90
B,70,70,70,80
C,90,90,70,70
D,60,70,80,90


【実行結果】
> python total.py
A 310
B 290
C 320
D 300

'''

DATA_FILENAME = 'test.csv'

# ファイルの読み込みです
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []                                        #1要素1人分のデータを入れるリスト
    title = f.readline()                                    #1行目の読み込み
    for line in f:                                          #残りの行を読み込み
        line = line.strip()                                 #行末の改行を取り除く
        person_data.append(line.split(','))                 #「,」で分割して格納
        # person_data.append(line.strip().split(','))       #まとめて書いてもOK


for data in person_data:                                    #各人のデータを1人分ずつ処理
    name, scores = data[0], data[1:]                        #名前と特典に分ける
    scores = [int(num) for num in scores]                   #文字列を数字に変換
    total = sum(scores)                                     #合計を求める
    print(name,total)                                       #1人分ずつ出力


import csv
import pprint

with open('./test.csv') as f:
    print(f.read())



