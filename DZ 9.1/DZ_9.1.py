print('Укажите длину списка для проверки')
n = int(input())
print('Введите', n, 'чисел через пробел')
s = list(map(int, input().split()))
if (len(s) > n):
    print('Введены лишние числа')
    exit()
elif (len(s) < n):
    print('Введено недостаточно чисел')
    exit()
tmp = set(s)
print('Введено', len(tmp), 'различных чисел')
