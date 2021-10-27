'''


[1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18]

'''


'''

# ・ P.217 の内包表記サンプル（以下）を通常の for で書いてください。
multiplication = [i * j for i in range(1,3) for j in range(1,10)]
print(multiplication)

'''


multiplication = []
for i in range(1,3):
    for j in range(1,10):
        multiplication.append(i * j)

print(multiplication)

