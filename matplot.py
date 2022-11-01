from pylab import *

x = linspace(0, 10, 5)
print(x)
y = x ** 2
print(y)

fig = plt.figure()
plot(x,y, 'r')
xlabel('x')
xlabel("y")
show()