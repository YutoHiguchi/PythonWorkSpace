'''

【実行結果】
> python func_1.py
[1, 2, 3, 4, 5, 6]
[4, 5, 6, 1, 2, 3]
引数がリストではありません
['a', [1, 2, 3]]
引数がリストではありません
[[1, 2, 3], 'xyz']
引数がリストではありません
[10, 'abc']

'''



def combine_list(list1, list2):
'''2 つのリストを結合し、リストで返す'''
# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))