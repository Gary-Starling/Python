#Цикл while
#Задача «Количество четных элементов последовательности»
#Условие
#Определите количество четных элементов в последовательности,
#завершающейся числом 0.

k = 0
x = int(input())

while x:
    if x % 2 == 0:
        k += 1
    x = int(input())
print(k)