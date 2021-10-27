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
    input_fruit = input("果物をカタカナで入力してください：")

    if input_fruit == '':
        break

# リストに追加するには？　p.64　fruits.append(input_fruit)

    if input_fruit in fruits:
            print(f'{input_fruit}は、知っています!')
    else:
        print(f'{input_fruit}は知りませんでした。覚えておきます。')
        fruits.append(input_fruit)


print('知っている果物')
print(fruits)
