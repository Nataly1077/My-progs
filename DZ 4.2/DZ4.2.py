﻿print('Введите пятизначное число.')
print('Программа возведёт количество десятков в степень количества единиц.')
print('Затем умножит это число на количество сотен.')
print('И разделит получившееся число на разность количества десятков тысяч и количества тысяч.')
num = int(input())
a = num // 10000
a1 = num % 10000
b = a1 // 1000
b1 = a1 %1000
c = b1 // 100
c1 = b1 % 100
d = c1 // 10
d1 = c1 % 10 
e = d1 % 10
print('Ответ:', ((d**e) * c) / (a - b))
