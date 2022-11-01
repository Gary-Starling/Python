
a = int(input())
b = int(input())

res = 1

while (res % a) or (res % b):
    res += 1
print(res)   

