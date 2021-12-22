'''

【実行結果】
> python deco_sample.py
test->10
[start]--
test->20
--[end]
[start]--
test->30
--[end]
[start]--
test2->100
--[end]

'''


def startend(func):
    def funcname(*args, **kwargs):
        print('[start]--')
        result = func(*args, **kwargs)
        print('--[end]')
        return result
    return funcname

def test(n):
    print('test->{}'.format(n))

# main
test(10)  # 通常の呼出

# デコレータ使用
deco_func = startend(test)
deco_func(20)

# 同一の関数名でデコレータ使用
test = startend(test)
test(30)

# @記法を使用
@startend
def test2(n):
    print('test2->{}'.format(n))

test2(100)
