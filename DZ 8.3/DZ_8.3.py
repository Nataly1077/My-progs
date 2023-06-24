
print('Введите грузоподъемность лодки')
m = int(input())
print('Введите количество рыбаков')
n = int(input())
c = 0
print('Введите вес каждого рыбака по отдельности')
t = sorted([int(input()) for _ in range(n)], reverse = True)
if t[0] > m:
    print('Задача не имеет решения')
    exit()
while len(t):
    c += 1
    k = m - t.pop(0)
    for i in range(len(t)):
        if t[i] <= k:
            t.pop(i)
            break
print('Потребуется', c, 'лодок')