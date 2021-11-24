while True:
    input_number = int(input("整数を入力して下さい（終了 -> 0）:"))

    if input_number == 0:
        break
    if input_number % 2 == 0:
        print("偶数です。")
    else:
        print("奇数です。")
