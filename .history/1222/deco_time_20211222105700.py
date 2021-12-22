'''

【実行結果】
> python deco_time.py
実行関数:test 実行時間： 3.002683162689209
実行関数:test 実行時間： 10.008330821990967

'''



import time
def run_time(func):

# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)

test(3)
test(5)

