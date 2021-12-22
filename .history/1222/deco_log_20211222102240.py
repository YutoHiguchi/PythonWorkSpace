'''

【実行例：画面】
test->100
test->0
test->1
test->2
test->3
test->4

【実行例：python.log】
2020-06-10 18:57:40.079496 function:test args:(100,) kwargs:{}
2020-06-10 18:57:40.079570 function:test args:(0,) kwargs:{}
2020-06-10 18:57:40.079598 function:test args:(1,) kwargs:{}
2020-06-10 18:57:40.079617 function:test args:(2,) kwargs:{}
2020-06-10 18:57:40.079635 function:test args:(3,) kwargs:{}
2020-06-10 18:57:40.079653 function:test args:(4,) kwargs:{}

'''


import datetime
def log_file(func):

# main
@log_file
def test(n):
    print('test->{}'.format(n))

# 呼出
test(100)

# 呼出
for i in range(5):
    test(i)


#現在の日付と日時
date = datetime.datetime.now()
print(date)