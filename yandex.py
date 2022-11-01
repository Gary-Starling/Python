'''1
Опишите словами алгоритм решения задачи
Ввод: натуральное число n
Вывод: количество простых чисел строго меньше n
Решение должно быть вычислительно-эффективным

Решение

Ввод числа n
k = 2     #Простое
div = []  #Пустой список делителей
cnt = 0  #Счётчик простых чисел

Пока k меньше n
   для i в div              # Перебор делителей
     если k % i == 0    # Если делится без остатка
       выход из цикла # Следо-но > 2 делителей выходим
   иначе(for python else)  # В списке не нашли делитель
    добавить k в список div #значит простое
    cnt += 1 #Увеличиваем счётчик делителей

Вывод числа
'''
''' Код на python 3.x '''
    #n = int(input()) #Меньше какого натурального числа выводим числа
    #k = 2 # Простые числа начинаются с 2
    #div = [] # Пустой список делителей
    #cnt = 0 #Счётчик простых чисел
#
    #while k < n:
    #    for i in div:
    #        if k % i == 0:
    #            break # Значит > 2 делителей
    #    else: #Не нашли делителей
    #        div.append(k)
    #        cnt += 1
    #    k += 1
#
    #print(cnt)


'''2
Дан неупорядоченный массив из печатных ASCII символов
Опишите своими словами (без кода и псевдокода) алгоритм сортировки, позволяющий упорядочить этот массив по алфавиту за линейное время
Необходимо описать действия на каждом шаге алгоритма
Возможен ли стабильный вариант такого алгоритма сортировки?

На самом деле хотелось решить "в лоб" быстрой сортировкой из библиотеки C или python, я немного знаком с big O,
поэтому понял что линейного решения я не добьюсь используя пузырёк или быструю сортировку. 
Поэтому я подумал про "Сортировку подсчётом"!

Итак, мы имеем печатные ascii символы, если взглянуть в таблицу то от a до z от 97 до 122 в dec(печатные символы).
Получается что каждый последующий символ имеет числовое значение, больше, чем предыдущее на 1.
Это говорит о том что мы можем пользовться ascii кодом, как индексом в массиве

а)Т.к. кодировка 256 символов мы создаём массив, заполненый нулямя asci[256], чтобы не усложнять алгоритм
б)Если список 100% по заданию "печатных символов", я опускаю проверку на другие символы

Алгоритм
1.Создать пустой массив беззнаковых целых чисел, размером 256
2.Идём проходом по массиву печатных неупорядоченных символов, от первого до последнего.
3.В каждой итерации цикла преобразуем символ в числовое значение таблицы acii.
  Берём это число и спользуем в пустом массиве из п.1 как индекс и добавляем в эту ячейку 1.
4.Когда проход закончится, мы получаем массив где в индексах от 97 до 122 какие-то
числовые значения.
5.Создаём новый проход (for1) от 97 до 122, с шагом 1(перебор значений внутри массива размером 256 с индексами от 97 до 122)
6.Внутри этого прохода, ещё один проход (for2)от 0 до цифрового значения в данной ячейке.
7.Если в ячейке 0 элементов, то мы перейдём к следующей итерации (for1)
8.Если не 0
  Берём индекс из прохода на уровень выше(for1), этот индекс является кодом символа,
преобразуем в символ и выводим(либо сохраняем в другой массив/строку) его столько раз, сколько записано в данной ячейке

Такой алгоритм будет всегда выполняться линейное время, т.к. проход сортировки всего один.

list_to_sort = 'cabcanmakdba'

asci_table = [0 for i in range(256)]

for sym in list_to_sort:
    asci_table[ord(sym)] += 1

for j in range(97, 122, 1):
    for k in range(asci_table[j]):
        print(chr(j), end='')
'''


'''3
Дан массив неповторяющихся чисел, который был отсортирован, а затем циклически сдвинут на неизвестное число позиций.
Опишите без кода и псевдокода алгоритм поиска максимума в таком массиве
Оцените сложность предложенного алгоритма
Изменится ли сложность если массив содержит повторяющиеся числа?

а)самый простой, но медленный способ,
выполнить поиск элемента простым перебором, взяв первый за максимум и сравнивать каждую итерацию,
если максимум, меньше следующего, максимуму присвоить следующий и т.д. O(n);

б)Второй способ, используя алгоритм бинарного поиска O(log n), нужно найти неотсортированный отрезок

Алгоритм
1.Выбираем левый и правый элемент 
2.Если самый левый элемент меньше самого правого, тогда сдивга нет(массив отсорирован) например [1,2,3,4,5,6]
вернём самый правый элемент, как максимум
3.Если это не так, например [5,6,1,2,3,4] (массив со сдвигом)
4.Находим центр массива, делим длину пополам это будет средний элемент
5.Сравниваем средний элемент с самым правым, тут три варианта
 если средний меньше самого правго элемента, это отсортированный отрезок, он нам не нужен,
 ставим самую правую точку отрезка(индекс), на место среднего.
 если средний элемент больше правого, это неотсортированный отрезок, нам он и нужен,
 ставим самую левую точку, вместо средней.
 если элементы по краям равны, на придётся перебирать все элементы подряд, в поисках MAX, O(n) - худший случай.
6.Мы выбрали неотсортированный отрезок, возращаемся к пункту 3(while или рекурсия),
  снова делим отрезок пополам и сравниваем крайние, так, пока не останется двух элементов,
  левый будет максимом.

Если будут повторяющиеся числа с концов массива, алгоритм будет работать медленнее O(n).
Т.к. мы не можем выбрать неотсортированный отрезок, а значит придётся искать прямым перебором.
'''


#mass1 = [1,2,3,4,5,6,7,8,9,10]
#mass2 = [7,8,9,10,1,2,3,4,5,6] # 
#mass3 = [6,7,8,9,10,1,2,3,4,5] # [10,1,2,3,4,5] # [10, 1, 2] # [10, 1]
#mass4 = [2,2,3,4,2,2,2,2,2,2,2]
#
#def search(arr):
#    left = 0
#    right = len(arr) - 1
#
#    if arr[left] < arr[right]: #Сдвига нет
#      return arr[right]
#    else:
#      while left < right - 1:
#        mid = int((left + right)/2)
#        if arr[mid] > arr[right]: # Если середина больше правого края max справа
#          left = mid
#        elif arr[mid] < arr[right]:
#          right = mid # Если середина правого края, max слева
#        else: #Если непонятно, то
#          max = arr[left]
#          left += 1
#          while left != right:
#            if max < arr[left]:
#              max = arr[left]
#            left += 1
#          return max
#
#    return arr[left]
#
#print(search(mass4))

'''4
Напишите регулярное выражение, которое позволяет выделить все строки отвечающие условиям:

Состоят только из букв
Одна и только одна из букв является заглавной

Пример строк которые могут быть выделены выражением:

"Мама",
"авТо",
"гриБ",
'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО'

Пример строк которые не должны быть выделены выражением:

"агент007" - содержит цифры
"стриж" - только строчные буквы
"ГТО", - более одной заглавной буквы
"Три богатыря" - содержит пробел, допустимы только буквы
'''



'''5
	
Дан указатель на корень двоичного дерева
Опишите словами алгоритм, который вернёт True если дерево является двоичным деревом поиска и False если не является

Вершина дерева содержит целочисленное значение (value) и два указателя на поддеревья (left и right).

В виде структуры на языке C это можно записать так:

struct node {
  int value;
  node* left;
  node* right;
'''

'''6
В реляционной базе данных существуют таблицы:

Cities - список городов

id - первичный ключ
name - название
population - численность населения
founded - год основания
country_id - id страны

Countries - список стран

id - первичный ключ
name - название
population - численность населения
gdp - валовый продукт в долларах

Companies - компании

id - первичный ключ
name - название
city_id - город в котором находится штаб-квартира
revenue - годовая выручка в долларах
labors - численность сотрудников

Постройте таблицу, где для каждой страны посчитано число компаний, удволетворяющих условиям:

1) штаб квартира компании находится в этой стране
2) число сотрудников компании не менее 1000 человек
'''



'''
Напишите регулярное выражение, которое позволяет выделить все строки отвечающие условиям:

Состоят только из букв
Одна и только одна из букв является заглавной

Пример строк которые могут быть выделены выражением:

"Мама",
"авТо",
"гриБ",
'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО'

Пример строк которые не должны быть выделены выражением:

"агент007" - содержит цифры
"стриж" - только строчные буквы
"ГТО", - более одной заглавной буквы
"Три богатыря" - содержит пробел, допустимы только буквы'''

# ^([а-я]*[А-Я][а-я]*)$
#  С регулярками у меня плоховато, но я написал такую используя https://regex101.com/

import re

#^ - начало строки
#$ - Конец строки
#{n} - ровно n раз символ
#

#^$

#\S любой символ кроме пробела

yes = "авТо"
no = "стриж"

arr_ok = ["Мама", "авТо","гриБ",'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО']
arr_err = ['агент007', 'стриж', 'ГТО', 'Три богатыря', 'ХоХо', 'оооооХ']


#for st in arr:
#  fullmatch = re.findall(r"[а-я]*\[А-Я]{1}", st)
#  print(fullmatch)
#print("---------------")
#
#for st in arr:
#  fullmatch = re.findall(r"[А-Я]{1}", st)
#  print(fullmatch)
#print("---------------")
#for st in arr:
#  fullmatch = re.findall(r"[^0-9]", st)
#  print(fullmatch)
#print("---------------")

for st in arr_ok:
  fullmatch = re.findall(r"^([а-я]*[А-Я][а-я]*)$", st) #Любое количество а-я начало, один заглавный символ, снова заглавные
  print(fullmatch)
print("---------------")
#"^([а-я]*[А-Я][а-я]*)$"
for st in arr_err:
  fullmatch = re.findall(r"^([а-я]*[А-Я][а-я]*)$", st) #Любое количество а-я начало, один заглавный символ, снова заглавные
  print(fullmatch)
print("---------------")



'''
Дан указатель на корень двоичного дерева
Опишите словами алгоритм, который вернёт True если дерево является двоичным деревом поиска и False если не является

Вершина дерева содержит целочисленное значение (value) и два указателя на поддеревья (left и right).

В виде структуры на языке C это можно записать так:

struct node {
  int value;
  node* left;
  node* right;
}

У бинарного дерева, в левой ветви значение всегда меньше, чем у родителя(узла),
в правой всегда больше, а так же нет повторений.
Значит нам надо проверить, идя от корня.
1.Если корень пуст или указатели left/right пустые, мы не имеем никаких значений,
но пока можно утверждать что это бин.дерево вернём true;
2.Проверить если левое значени root-left->val(левая ветка) больше или равно root->val(корень)
если да, вернуть false, нет, идём дальше
3.Проверить что root->right->val(правая ветка) меньше или равна root->val
если да, вернуть false, нет, идём дальше
4.Перемещамся к левой и правой ветке и переходим к пункту 1.
Сложно описать этот пункт, попробую так,
Через логическое && мы рекурентно запускаем внутри функции проверки
саму себя два раза return( IsBin(root->left) && IsBin(root->right))
Таким образом мы проверим всё дерево и в каком-либо узле, условие не совпадёт,
мы вернём false;
'''