# Арифметические операции
# +,-,/,%,//,**
# Приоритет операции
# **,*,/,//,%,+,-
# () Скобы меняют приоритет 

a = 12
b = 8
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a // b
print(c)
c = a % b
print(c)
c = a ** b
print(c)
d = 1.3
e = 2
k = (d ** e)
print(k)
k = round(d ** e) # округление результата
print(k)
k = round(d ** e, 3) # округление результата 3числа
print(k)

n = 5
n = n + 3
print(n)
n = 5
n += 3 # сокращенные операции
print(n)
n = 5
n *= 3 # сокращенные операции
print(n)