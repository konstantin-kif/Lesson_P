# Анонимные, lambda функции

import re


def f(x):
    x ** 2
g = f
print(type(f)) # смотреть что выдает
print(f(1))
print(g(1))

def f(x):
    return x ** 2
g = f
print(f(2))
print(g(4))

def calc1(x):
    return x + 10
print(calc1(10))

def calc2(x):
    return x * 10
print(calc2(10))

def math(op, x):
    print(op(x))

math(calc1, 10)
math(calc2, 10)

def sum(x, y):
    return x + y 

sum = lambda x, y: x + y

def mylt(x, y):
    return x * y

f = mylt

def calc(op, a, b):
    print(op (a, b))
    # return(op, a, b)

calc(mylt, 4, 5)
calc(f, 5, 5)
calc(sum, 6, 5)
calc(lambda x, y: x + y, 6, 5)