print('Введите число')
num = int(input())
if num == 0:
    print('нулевое число')
elif (num <= 0) and (num % 2 == 0):
    print('отрицательное четное число')
elif (num >= 0) and (num % 2 == 0):
    print('положительное четное число')
else:
    print('число не является четным')
