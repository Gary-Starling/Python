#Цикл while#
#Задача «Числа Фибоначчи»



n_it = int(input())
n = 2
t1 = 1 
t2 = 1
t3 = 0

if n_it == 1 or n_it == 2:
    print(t1)
else:
    while n < n_it:
        t3 = t2 + t1
        t1, t2 = t2, t3
        n += 1
    print(t3) 
