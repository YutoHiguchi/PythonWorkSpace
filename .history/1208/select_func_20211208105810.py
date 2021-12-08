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
    type = input("どちらを実行しますか？：")

    print(run_list.keys()) #dict_keys(['a', 'b'])

    # if type == "":
    #     break
    # elif type == "a":

