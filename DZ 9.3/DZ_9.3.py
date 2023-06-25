print('Введите последовательность чисел через пробел. Если оно уже встречалось - выведется YES, если нет - NO')
numbers = [int(s) for s in input().split()]
before = set()
for num in numbers:
    if num in before:
        print(num, 'YES')
    else:
        print(num, 'NO')
        before.add(num)
