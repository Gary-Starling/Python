#Задача «Замена внутри фрагмента»
#Условие
#Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

s = str(input())

first = s.find('h')
second = s.rfind('h')

str_new = s[0:first+1:1] + s[first+1:second:1].replace('h', 'H') + s[second::1]
print(str_new)
