'''
【実行結果】

> python sample_3.py
----------
[('S', 1), ('S', 2), ('S', 3), ('S', 4), ('S', 5), ('S', 6), ('S', 7),
('S', 8), ('S', 9), ('S', 10), ('S', 11), ('S', 12), ('S', 13), ('H', 1),
('H', 2), ('H', 3), ('H', 4), ('H', 5), ('H', 6), ('H', 7), ('H', 8),
('H', 9), ('H', 10), ('H', 11), ('H', 12), ('H', 13), ('C', 1), ('C', 2),
('C', 3), ('C', 4), ('C', 5), ('C', 6), ('C', 7), ('C', 8), ('C', 9),
('C', 10), ('C', 11), ('C', 12), ('C', 13), ('D', 1), ('D', 2), ('D', 3),
('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8), ('D', 9), ('D', 10),
('D', 11), ('D', 12), ('D', 13)]
----------
選んだカードは('S', 5)です

'''


# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [] # デッキ用リスト
for
for
print('-'*10)
print(cards)
print('-'*10)
# 1 枚選択
import random # 乱数用モジュール
r = random.randrange(52) # 0〜51 の乱数生成
print(f'選んだカードは{cards[r]}です')

