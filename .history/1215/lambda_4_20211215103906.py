'''

【実行結果】
> python lambda_3.py
[('C', 13), ('C', 10), ('S', 8), ('S', 6), ('H', 5)]

'''



import random # 乱数用モジュール

'''

o カードから、5 枚のカードをランダムに選択する。
o カードを数字の大きい方から並べ、出力する。
    sort の key に関してはテキスト P.183 を良く理解しよう！

'''


# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [] # デッキ用リスト

for m in marks:
    for n in range(1,14):
        t = (m,n) # タプルでカード生成
        cards.append(t) # リストに追加



# 5 枚選択
select_cards = random.sample(cards, 5)
# 並び替え
select_cards.sort(reverse=True, key=lambda x: x[1])

# 出力
print(select_cards)





# print('-'*10)
# # cards.sort(reverse=True) #順序をソート、逆順の場合引数にreverse=Trueを入れる
# print(cards)
# print('-'*10)


# # 1枚選択
# import random				# 乱数用モジュール
# r = random.randrange(52)	# 0〜51の乱数生成
# print(f'選んだカードは{cards[r]}です')
# print(f'選んだカードは{random.choice(cards)}です')  # 実は1行で書ける