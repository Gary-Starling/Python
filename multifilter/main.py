#Упражнение на итераторы

if __name__ == '__main__':

    class multifilter:
        def judge_half(pos, neg):
            # допускает элемент, если его допускает хотя бы половина функций (pos >= neg)
            return pos >= neg

        def judge_any(pos, neg):
            # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
            return pos >= 1

        def judge_all(pos, neg):
            # допускает элемент, если его допускают все функции (neg == 0)
            return neg == 0

        def __init__(self, iterable, *funcs, judge=judge_any):
            # iterable - исходная последовательность
            # funcs - допускающие функции
            # judge - решающая функция
            self.iterable = iterable
            self.funcs = funcs
            self.judge = judge

        def __iter__(self):
        # возвращает итератор по результирующей последовательности
            for element in self.iterable:
                pos = 0
                neg = 0
                for func in self.funcs:
                    if func(element):
                        pos += 1
                    else:
                        neg += 1
                if self.judge(pos, neg):
                    yield element



    def mul2(x):
        return x % 2 == 0

    def mul3(x):
        return x % 3 == 0

    def mul5(x):
        return x % 5 == 0

    def test_gen(k):
        for i in range(k):
            yield i

    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    #1 3 5 7 9 11 13 15 div 2
    # 
    #Генератор простых чисел
    def primers1():
        n, dividers = 2,[]
        while True:
            for i in dividers:
                if n % i == 0:
                    break
            else:
                dividers.append(n)
                yield n
            n += 1


            


    easy_dig = primers1()
    for i in range(1, 1000, 1):
        print(next(easy_dig))

'''    gen = test_gen(4)
    for i in gen:
        print(i)
    a = [i for i in range(31)] # [0, 1, 2, ... , 30]

    print(list(multifilter(a, mul2, mul3, mul5))) 
    # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

    print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
    # [0, 6, 10, 12, 15, 18, 20, 24, 30]

    print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
    # [0, 30]
    '''
