from numpy import *


mass = array([1,2,3,5])
print(mass)
print(mass.ndim)
print(mass.shape)

new = zeros((3,3))
print(new)

big_mass = arange(100, 300, 10)
print(big_mass)

a = array([10,20,30])
b = array([5, 10, 15])
print(a + b)
print(a - b)
print(a ** 3)
print(sin(a))