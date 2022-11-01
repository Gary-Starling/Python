#Занятие 11. Словари
#Задача «Страны и города»
#Условие
#Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

n = int(input())
country = {}

for i in range(n):
    str = input().split()
    for j in range(1,len(str),1):
        if str[0] in country:
            country[str[0]] += [str[j]]
        else:
            country[str[0]] = [str[j]]

cnt = int(input())
for i in range(cnt):
    city = input()
    for j,k in country.items():
        if city in k:
            print(j)
