'''

【実行例】
> python func_sample.py
引数は 0 個です。受け取った値は()です
引数は 1 個です。受け取った値は(10,)です
引数は 2 個です。受け取った値は(10, 20)です
引数は 3 個です。受け取った値は(10, 'a', 'xyz')です
引数は 2 個です。受け取った値は(10, [1, 2, 3])です

'''




def any_items(*args):
    items_count = len(args)
    print(f'引数は{items_count}個です。受け取った値は{args}です')

any_items()
any_items(10)
any_items(10, 20)
any_items(10, 'a', 'xyz')
any_items(10, [1, 2, 3])