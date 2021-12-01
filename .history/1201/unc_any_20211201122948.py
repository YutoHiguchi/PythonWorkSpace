'''

【実行結果 1】
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： L,カレー
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： D,ステーキ
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： B,トースト
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：
['トースト', 'カレー', 'ステーキ']

'''

'''

【実行結果 2】
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： B,小倉トースト
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： D,中華飯
朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：
['小倉トースト', '-', '中華飯']

'''


def out_csvdata(**kwargs):
    out_list = []
    for token in ['B', 'L', 'D']:
        if token in kwargs.keys():
            out_list.append(kwargs[token])
        else:
            out_list.append('-')

    # print(out_list)
    print(",".join(out_list))


# main
eat = {}
while True:
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください： ")
    if menu == '':
        break

    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        12
        eat[token] = menu

    else:
        print('記号が間違っています。登録しません')
        continue


out_csvdata(**eat)
