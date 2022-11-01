#Списки
#Задача «Переставить min и max»
#Условие
#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
s = input()  # 
A = s.split(' ')
ind_min = 0;
ind_max = 0;
max = min = int(A[0])
for i in range(0, len(A), 1):
    if int(A[i]) > max:
        max = int(A[i])
        ind_max = i
    if int(A[i]) < min:
        min = int(A[i])
        ind_min = i
A[ind_max], A[ind_min] = A[ind_min], A[ind_max]
print(' '.join(A))
