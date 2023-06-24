print('Введите любое число от 1 до 10000')
n = int(input())
print('Введите', n, 'целых чисел')
s = []
for i in range(n):
    s.append(int(input()))
s.reverse()
print(s)