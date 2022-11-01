#Двумерные массивы
#Задача «Шахматная доска»
#Условие
#Даны два числа n и m.
# Создайте двумерный массив размером n×m и заполните его
#символами "." и "*" в шахматном порядке. В левом верхнем
#углу должна стоять точка.

n, m = [int(i) for i in input().split()]
a = []
a = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j)%2:
            a[i][j] = '*'
        else:
            a[i][j] = '.'

for i in range(len(a)):  
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()    

