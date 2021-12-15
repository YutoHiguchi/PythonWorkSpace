'''

【実行結果】
> python lambda_3.py
['hello', 'nice', 'abc', 'test', 'morning', 'good', 'yes', 'world']
['hello', 'morning', 'world']

'''


my_list = ['hello','nice','abc','test','morning','good','yes','world']
'''5文字以上のリストを作成する'''

new_list = list(filter(lambda x:filter_5,my_list))


def filter_5(i):
    if i >= 5:
        return True
    else:
        return False

print(my_list)
print(new_list)