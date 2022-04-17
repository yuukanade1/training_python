# 1 出力の仕方
print('Hello, world!!')

# 2 演算子
print(1 + 2)
print(3 - 2)
print(5 * 2)
print(5 / 2)
print(5 % 2) # 割り算の余り
print(5 // 2) # 割り算の商のみ
print(5 ** 2) # べき乗

# 3 if文
point = 80
if point >= 80:
    print('合格')
print('--')

# 4 if~else
point = 79
if point >= 80:
    print('合格')
else:
    print('不合格')

# 5 elif(else ifのこと)
point = 79
if point >= 80:
    print('合格')
elif point >= 60:
    print('保留')
else:
    print('不合格')

# 6 比較演算子
point = 100
if point == 100:
    print('100点おめでとう。') # 等しい

point = 100
if point != 100:
    print('100点ではありません。') # 等しくない
