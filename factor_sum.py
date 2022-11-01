#Условие
#По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено.

N = int(input())

mul = 1
sum_factor = 0

for i in range(1, N + 1):
    mul *= i
    sum_factor += mul
    
print(sum_factor)

