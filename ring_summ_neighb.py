#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
#Для решения задачи может пригодиться метод sort списка.
#Выводимые числа не должны повторяться, порядок их вывода может быть произвольный
s = input()  # 
A = s.split(' ')
if len(A) == 1:
    print(int(A[0]))
else:    
    for i in range(0, len(A), 1):
        print(int(A[i-1]) + int(A[(i+1)%len(A)]), end= ' ')

