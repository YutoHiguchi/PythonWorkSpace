'''

【実行例】
> python choice.py
数字を入力してください。（0：終了） 10
偶数
数字を入力してください。（0：終了） 13
奇数
数字を入力してください。（0：終了） ab
入力が正しくありません
数字を入力してください。（0：終了） 0

'''


def odd():
    print("奇数")

def even():
    print("偶数")

def choice_func(number):
    # if number == 0:


    if number % 2 == 0:
        return even()
    else:
        return odd()

    return func


# main
while True:
    num = input("数字を入力してください。（0：終了） ")
    if num.isnumeric():
        num = int(num)
    else:
        print("入力が正しくありません")
        continue
    if num == 0:
        break

    print(choice_func(num))
