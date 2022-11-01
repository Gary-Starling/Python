# Двумерные массивы
#Задача «Поменять столбцы»
#Условие
#Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
#Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
#Решение оформите в виде функции swap_columns(a, i, j).

def swap(a, i, j):
    for y in range(len(a)):
        a[y][i], a[y][j] = a[y][j], a[y][i]

n, m = [int(i) for i in input().split()]

a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

i, j = [int(i) for i in input().split()]   

swap(a,i,j)
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
