input = open('Бодрых_А_В_ЗИТ22м_vvod.txt').read().splitlines()
output = open('Бодрых_А_В_ЗИТ22м_vivod.txt', "w",encoding='utf-8')
s = [line.split() for line in input]
#Определение начала и окончания чтения массивов
print(s)
matrix = [line.split() for line in input[:len(s)]]
print(matrix)
#8
#1. Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
arr=[]
for i in range (len(s)):
    maxsum = 0
    for j in range(len(s)):
       #print(int(matrix[i]))
        maxsum+=int(matrix[i][j])
    arr.append(maxsum)
#for i in range (5): maxsum[i]=sum(matrix[i])
output.write(f'MIN cтрока {arr.index(min(arr))+1} сумма {min(arr)}')
output.write(f' MAX cтрока {arr.index(max(arr))+1} сумма {max(arr)} ')


#2. Дана квадратная матрица A[N, N], Записать на место отрицательных элементов матрицы нули,
# а на место положительных — единицы. Вывести на печать нижнюю треугольную матрицу в общепринятом виде.

input = open('Бодрых_А_В_ЗИТ22м_vvod1.txt').read().splitlines()
output = open('Бодрых_А_В_ЗИТ22м_vivod1.txt', "w",encoding='utf-8')
s = [line.split() for line in input]
#Определение начала и окончания чтения массивов
#print(s)
a = [line.split() for line in input[:len(s)]]
#print(matrix)
a1=[]
b1=[]
for i in range (len(s)):
    a1 = []
    for j in range(len(s)):
       #print(int(matrix[i]))
        a1.append(int(a[i][j]))
    b1.append(a1)

print(b1)
b1 = [[1 if x>0 else 0 for x in i] for i in b1]
print(b1)

f = [list(map(str, i)) for i in b1]



for i in range(len(b1)):
    for x in range(len(b1)):
        if x > i:
           f[i][x] = ' '

for i in range(len(f[0])):
    output.write(str(f[i])+'\n')

