'''

【実行結果】
> python lambda_1.py
[1, 3, 5, 7, 2, 4, 6, 8]
[10, 30, 50, 70, 20, 40, 60, 80]

'''

my_list = [1, 3, 5, 7, 2, 4, 6, 8]

#list
# 受け取ったイミデータを基にリストを作成する


#map
# 繰り返し処理をシンプルに

new_list =  list(map(lambda x: x*10, my_list))

print(my_list)
print(new_list)