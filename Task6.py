import random

#1. Дан массив целых чисел. Найти максимальный элемент массива и его порядковый номер.
print('Введите кол во чисел массива')
n = int(input())
print('Введите значения массива')
max_value = int(input())
index = 0
for k in range(n-1):
    po = int(input())
    if po > max_value:
        max_value = po
        index = k+1
print('Максимальное значение '+str(max_value))
print('Индекс '+str(index))
# 2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из нечетных чисел исходного массива или сообщить, что таких чисел нет. Полученный массив вывести в порядке убывания элементов.
print('Задача 2')
mass = [random.randint(0, 50) for _ in range(20)] #создаём массив случайных чисел
print(mass)
res = []
for el in mass:
    if el % 2 != 0:
        res.append(el)
if len(res) == 0:
    print('No numbers')

print(sorted(res, reverse=True))
