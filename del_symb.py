#Условие
#Дана строка. Удалите из этой строки все введённые символы


print('enter string')
s = str(input())
print('enter symbol')
sym = str(input())

new_s = s.replace(sym, '')
print(new_s)
