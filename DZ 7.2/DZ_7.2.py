x = input("введите строку: ")
while '  ' in x:
    x = x.replace('  ', ' ')
print(x)