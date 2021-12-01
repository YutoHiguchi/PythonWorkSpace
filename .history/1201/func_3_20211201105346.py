'''

【実行結果】
> python func_3.py
受け取った値： ()
やること無いので暇です7
受け取った値： (10,)
20
受け取った値： ('asdfg',)
asdfgasdfg
受け取った値： ([1, 2, 3],)
難しくて無理です
受け取った値： (10, 20)
30
受け取った値： (10, 'abc')
できません〜
受け取った値： ('x', 'yz')
xyz
受け取った値： ([1, 2, 3], [4, 5, 6])
無茶言わないで！
受け取った値： (1, 2, 3)
無理です...

'''


def do_anything(*args):
    '''引数の個数によって何かする。 int と str で動作'''
    item_len = len(args)
    print(f'受け取った値：{args}')
    if item_len == 0:
        print('やること無いので暇です。')
    elif item_len == 1:
        if type(args) == str:
            print(f'{args}{args}')
        elif args.isdecimal():
            print(f'{args*2}')
        else:
            print('難しくて無理です')


# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)

