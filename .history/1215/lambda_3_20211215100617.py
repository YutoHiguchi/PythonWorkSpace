'''

【実行結果】
> python lambda_3.py
['hello', 'nice', 'abc', 'test', 'morning', 'good', 'yes', 'world']
['hello', 'morning', 'world']

'''


my_list = ['hello','nice','abc','test','morning','good','yes','world']
'''5文字以上のリストを作成する'''

new_list = list(map(lambda x:str(x),my_list))

print(my_list)
print(new_list)