word = list(input("Введите слово из маленьких латинских букв:"))

lenght = len(word)
a = 0
e = 0
i = 0
o = 0
u = 0

if 'a' in word:
    a +=1
if 'e' in word:
    e +=1
if 'i' in word:
    i +=1
if 'o' in word:
    o +=1
if 'u' in word:
    u +=1
elif not 'a' or 'e' or 'i' or 'o' or 'u' in word:
    print(False)
print("Количество гласных букв:", a+e+i+o+u)
print("Количество согласных букв:", (lenght - (a+e+i+o+u)))
print('Количество букв "a"', a)
print('Количество букв "e"', e)
print('Количество букв "i"', i)
print('Количество букв "o"', o)
print('Количество букв "u"', u)
