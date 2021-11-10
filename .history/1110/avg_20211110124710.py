'''

【実行結果】
> python avg.py
['国語', '算数', '理科', '社会']
[67.5, 77.5, 77.5, 82.5]
'''


# ↓先生の回答

DATA_FILENAME = 'test.csv'
person_data = []

# fileの読み込み
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    title = f.readline().strip().split(',') #1行目を読み込み
    for line in f:  #残りの行を全て読み込み
        person_data.append(line.strip().split(','))


print('person_dataは', person_data)


col = 1     #[0]は名前なのでSkip[1]から
avg = [0] * len(title)      #平均を格納するリスト
while col < len(title):
    for score in person_data:       #全員分の科目得点の処理
        avg[col] += int(score[col])/len(person_data)
    col += 1    #次の科目

print(title[1:])
print(avg[1:])


# ↑先生の回答










# DATA_FILENAME = 'test.csv'

# with open(DATA_FILENAME, 'r', encoding='utf8') as f:
#     person_data = []                                                #1要素1人分のデータを入れるリスト
#     title = f.readline()                                            #1行目の読み込み
#     for line in f:                                                  #残りの行を読み込み
#         line = line.strip()                                         #行末の改行を取り除く
#         person_data.append(line.split(','))                         #「,」で分割して格納
#         # person_data.append(line.strip().split(','))               #まとめて書いてもOK


# for data in person_data:                                            #各人のデータを1人分ずつ処理
#     name = data[0]
#     kokugo = data[1]
#     sansu = data[2]
#     rika = data[3]
#     shakai = data[4]                                                #名前と特典に分ける
#     scores_kokugo = [int(num_kokugo) for num_kokugo in kokugo]                           #文字列を数字に変換
#     scores_sansu = [int(num_sansu) for num_sansu in sansu]
#     scores_rika = [int(num_rika) for num_rika in rika]
#     scores_shakai = [int(num_shakai) for num_shakai in shakai]



#     total = sum(scores_kokugo, scores_sansu)                                             #合計を求める
#     avg = total/4
#     print(name,total)                                               #1人分ずつ出力






