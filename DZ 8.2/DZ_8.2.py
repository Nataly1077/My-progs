﻿print('Введите число от 1 до 100000')
n = int(input())
print('Введите', n, 'чисел в одну строку через пробел')
s = list(map(int, input().split()))
s.insert(0, s.pop())
print(s)
