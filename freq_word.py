'''
Словари
Задача «Самое частое слово»
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
'''

def sort_uniq(string, d):
    for item in string.split():
        if item in d:
            d[item][0] += 1
        else:
            d[item] = [1]
    return d    

d = {}
n = int(input())
for i in range(n):
    stroka = input()
    sort_uniq(stroka,d)
    
max = (sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True))
mass= []
maximum = max[0][1]
#print(maximum)
for i in max:
    if i[1] == maximum:
        mass.append(i[0])
print(min(mass))

