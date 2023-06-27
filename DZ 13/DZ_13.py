from random import randint
print('Введите количество строк матрицы:')
n = int(input())
print('Введите количество столбцов матрицы:')
m = int(input())

matrix_1 = [[randint(1, 10) for j in range(m)] for i in range(n)]
matrix_2 = [[randint(1, 10) for j in range(m)] for i in range(n)]

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j]  for j in range
(len(matrix_1[0]))] for i in range(len(matrix_1))]
 
print('Матрица # 1:')
print(matrix_1)
print('Матрица # 2:')
print(matrix_2)
print('Результат сложения матриц:')
print(matrix_3)