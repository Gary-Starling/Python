# simple calculator
# +, -, /, *, mod, pow, div, где
x = float(input())
y = float(input())
operation = str(input())



if(operation == '+'):
    print(x+y)
    
elif(operation == '-'):
    print(x-y)    

elif(operation == '/'):
        if y == 0:
            print('Деление на 0!')
        else:
            print(x/y)

elif(operation == '*'):
    print(x*y)

elif(operation == 'mod'):
        if y == 0:
            print('Деление на 0!')
        else:
            print(x%y)   

elif(operation == 'pow'):
    print(x**y)

elif(operation == 'div'):
        if y == 0:
            print('Деление на 0!')
        else:
            print(x//y)   
