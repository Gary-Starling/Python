# put your python code here
fig = input()

if fig == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ( a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif fig == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)    
else: #круг
    r = int(input())
    print(((r) ** 2) * 3.14)
          
