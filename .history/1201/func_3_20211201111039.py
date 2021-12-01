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
    # item_len = len(args)
    print(f'受け取った値：{args}')
    if len(args) == 0:
        print('やること無いので暇です。')
    elif len(args) == 1:
        args1 = args
        if type(args1) != int or type(args1) != str:
            print('難しくて無理です')
        else:
            print(args1 * 2)

        # if type(args) == str:
        #     print(f'{args}{args}')
        # elif args.isdecimal():
        #     print(f'{args*2}')
        # else:
        #     print('難しくて無理です')

    elif len(args) == 2:
        args1, args2 = args
        if type(args1) == type(args2) != int and type(args1) == type(args2) != str:
            print('無茶言わないで！')

        elif type(args1) != type(args2):
            print('できません～')

        else:
            print(args1 + args2)

    else:
        print('無理です...')

# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)

