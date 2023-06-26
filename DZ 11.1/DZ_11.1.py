def factorial(n):
    from math import factorial
    s = []
    num = factorial(n)
    for i in range(num, 0, -1):
        a = factorial(i)
        s.append(a)
    print('Список факториалов от факториала числа', n, ':', s)

print('Введите число')
n = int(input())
factorial(n)
