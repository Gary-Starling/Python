#Выведите таблицу размером n×n, заполненную числами от 1 до n^2 
#по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
#Sample Input:
#5
#Sample Output:

#1 2 3 4 5
#16 17 18 19 6
#15 24 25 20 7
#14 23 22 21 8
#13 12 11 10 9

n = int(input())
a = [[0] * n for i in range(n)]
cnt = 1
iters_inc = 0

start = 0
end = len(a) - 1
ptr = 0
x = ptr
y = 0


while(cnt < n*n):
    for i in range(start + iters_inc, end - iters_inc, 1):
        a[x + iters_inc][i] = cnt #по y ->
        cnt += 1
        ptr += 1  
    y = ptr
    ptr = 0
    
    for j in range(start + iters_inc, end - iters_inc, 1):
        a[j][y + iters_inc] = cnt # по x вниз
        cnt += 1
        ptr += 1   
    x = ptr
    ptr = 0
    
    for i in range(end - iters_inc, start + iters_inc,-1):
        a[x + iters_inc][i] = cnt #по у <-
        cnt += 1  
    y = ptr
    ptr = 0
    
    for j in range(end - iters_inc, start + iters_inc,-1):
        a[j][y + iters_inc] = cnt #по x вверх
        cnt += 1
    x = ptr
    ptr = 0
    iters_inc += 1  

if n != 0:
    if n % 2 != 0:
        a[n//2][n//2] = cnt
        
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = '  ')
        print()     
