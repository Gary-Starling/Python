#оптимальное умножение



def Multiply1(x, y):
    if y == 0:
        return 0
    z = Multiply1(x, int(y/2))    
    if y % 2 == 0:
        return (2 * z)
    else:
        return (x + (2 * z))

def Multiply2(a, b):
    if not b:
        return 0
    c = Multiply2(a, b >> 1)
    return a + (c << 1) if b & 1 else c << 1        


print("Enter x and y")
a, b = input().split()
a = int(a)
b = int(b)
print("x * y =", Multiply1(a,b))
print("x * y =", Multiply2(a,b))
