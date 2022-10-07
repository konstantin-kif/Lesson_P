# Кортежи - это неизменяемый список

import colorsys
from turtle import color


t = ()
print(type(t))
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (20, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors)
t = tuple(colors)
print(t)

(a) = (3, 4, 41, 5) # кортеж пишется с запятой
print(a)
print(a[1])  # 1 обозначает номерацию масива
print(a[-1]) # -1 обозначает последнее число масива

t = tuple(['red', 'green', 'blue'])
print(t[0])
print(t[2]) 
print(t[-2])

for e in t:
    print(e)

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('x:{} g:{} b:{}'.format(red, green, blue))
