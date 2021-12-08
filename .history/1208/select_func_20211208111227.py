'''

【実行例】
a=>Hello,b=>Goodbye
どちらを実行しますか？ :a
Hello
a=>Hello,b=>Goodbye
どちらを実行しますか？ :b
Goodbye
a=>Hello,b=>Goodbye
どちらを実行しますか？ :c
どちらかを選択してください。
a=>Hello,b=>Goodbye
どちらを実行しますか？ :

'''


# 関数を辞書で渡し、実行する
def func1():
    print("Hello")

def func2():
    print("Goodbye")

# main
run_list = {'a': func1, 'b': func2}


while True:
    print("a=>Hello,b=>Goodbye")
    select = input("どちらを実行しますか？：")

    # p.104 制御構文について
    if select == " ":   #入力された文字が空文字だった時
    # if select == " " or select == "" or select == "　":
        break

    if select in run_list.keys():   #run_list(辞書)のkeyに入力値が存在する時
        run_list[select]()
    else:
        print("どちらかを選択して下さい")





# print(run_list.keys()) #dict_keys(['a', 'b'])