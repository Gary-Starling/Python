a = int(input())
b = int(input())
c = int(input())

if a - b <= 0:
    max = b
else:
    max = a

if max - c <= 0:
    max = c

if a - b > 0:
    min = b
else:
    min = a

if min - c > 0:
    min = c

print(max)
print(min)
print((a + b + c) - (max + min))