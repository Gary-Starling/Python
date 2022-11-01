a = int(input())
b = int(input())

ost = 1

if a > b:
    ost = a % b
else:
    ost = b % a   

while ost: 
    a = b
    b = ost 
    ost = a % b
print(b)  

   
