#8
#1. Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
from random import randint
size = int(input('Размер матрицы? '))
matrix = [[randint(1,99) for x in range(size)] for _ in range(size)]
print(matrix)
for i in range (size): print(*matrix[i])
maxsum=[0]*size
for i in range (size): maxsum[i]=sum(matrix[i])
print (f'MIN cтрока {maxsum.index(min(maxsum))+1} сумма {min(maxsum)}')
print (f'MAX cтрока {maxsum.index(max(maxsum))+1} сумма {max(maxsum)} ')

#2. Дана квадратная матрица A[N, N], Записать на место отрицательных элементов матрицы нули,
# а на место положительных — единицы. Вывести на печать нижнюю треугольную матрицу в общепринятом виде.

from random import randint
print('Задача 2')
size = int(input('Размер матрицы? '))
a = [[randint(-10,10) for x in range(size)] for _ in range(size)]
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')
