import math

input_angle = float(input('角度を入力してください（度）： '))

angle = input_angle * math.pi / 180
a = math.sin(input_angle)
print(f'{input_angle}度 -> {angle}ラジアン')
print(f'sin({input_angle}) => {math.sin(angle)}')