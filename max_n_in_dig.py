#Задача на программирование: различные слагаемые
n = int(input())
ls = []
i = 1

while n > i*2:
    n -= i
    ls.append(i)
    i += 1
ls.append(n)
print(len(ls))    
print(*ls)    
