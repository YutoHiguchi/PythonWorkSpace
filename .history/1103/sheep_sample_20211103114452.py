# text P.131 の一部
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z']
print(alphabet)
# range を使用する 文字コードに注意
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabet)
# そもそも値を変更しないなら …
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet)
# 一応リストにするなら
alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']
print(alphabet)