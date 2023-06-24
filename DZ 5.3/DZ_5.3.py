x = int(input("Введите минимальную сумму инвестиций:"))
m = int(input("Введите Количество денег у Майка:"))
i = int(input("Введите Количество денег у Ивана:"))

if m >= x and i >= x:
    print('2')
elif m >= x and i <= x:
    print('Mike')
elif i>=x and m <= x:
    print('Ivan')
elif (m < x and i < x) and m + i >= x:
    print('1')
else:
    print('0')