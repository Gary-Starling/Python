#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
#Программа получает на вход целые числа P, X, Y и должна вывести два числа:
#величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.

P = int(input())
x = int(input())
y = int(input())

vklad = ((x * 100) + y)  * (P/100) + (x * 100) + y
print(int(vklad//100),int(vklad%100))
