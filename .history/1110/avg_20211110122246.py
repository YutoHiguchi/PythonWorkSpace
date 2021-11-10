'''

【実行結果】
> python avg.py
['国語', '算数', '理科', '社会']
[67.5, 77.5, 77.5, 82.5]
'''

DATA_FILENAME = 'test.csv'

with open(DATA_FILENAME, 'r', encoding='utf8') as f:
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






