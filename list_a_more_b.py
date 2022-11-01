#Списки
#Задача «Больше предыдущего»

s = input()  # 
A = s.split(' ')
for i in range(1, len(A), 1):
    if int(A[i]) > int(A[i-1]):
        print(A[i])