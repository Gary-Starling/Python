#Множества
#Задача «Полиглоты»
#Условие
#Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
#В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, которое он знает, а затем - названия языков, по одному в строке.
#В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.

n = int(input())
a = []
for i in range(0,n,1):
    a.append(i)
    a[i] = set()
    for j in range(int(input())):
        a[i].add(input())
 
all_lang = set()
one_sch = set()
for i in range(len(a)):
    all_lang.update(a[i])
#Язык у всех
for i in range(len(a)):
    all_lang.intersection_update(a[i])
    one_sch.update(a[i])

a = list(all_lang)  
a.sort()
print(len(a))   
print('\n'.join(a))
b = list(one_sch)
b.sort()
print(len(b))  
print('\n'.join(b))
