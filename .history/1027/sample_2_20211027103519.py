'''
【実行結果】

果物をカタカナで入力してください：リンゴ
リンゴは、知っています！
果物をカタカナで入力してください：イチゴ
イチゴは、知りませんでした。覚えておきます。
果物をカタカナで入力してください：イチゴ
イチゴは、知っています！
果物をカタカナで入力してください：パイナップル
パイナップルは、知りませんでした。覚えておきます。
果物をカタカナで入力してください：
知っている果物
['バナナ', 'リンゴ', 'オレンジ', 'イチゴ', 'パイナップル']

'''


fruits = ['バナナ','リンゴ','オレンジ']
while True:
    # print(fruits)
    a = input("果物をカタカナで入力して入力してください：")

    if a == '':
        break

# リストに追加するには？　p.64　fruits.append(input_fruit)

    if a in fruits:
            print(f"{a}は、知っています!")

print('知っている果物')
print(fruits)
