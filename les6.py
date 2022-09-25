# Управляющие конструкции While (пока)
# Цикл позволяет выполнять блок операторов какое-то количесиво раз
# While condition: (пока условие)
#    operator 1
#    operator 2
#    .........
#    operator n

from typing import List


original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# Управляющие конструкции цикл while-else (пока-ещё)
# While condition: (пока условие)
#    operator 1
#    operator 2
#    .........
#    operator n
# else: (ещё)
#    operator n + 1
#    operator n + 2
#    .........
#    operator n + m

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

# Управляющие конструкции цикл for (для)
# for i in enumeration: (для i в итерируемый объект)
#    operator 1
#    operator 2
#    .........
#    operator n

for i in 1,2,3,4,5:
    print(i**2)

list = [1,2,3,10,5]
for i in list:
    print(i)

r = range(5)
for i in r:
    print(i)

for i in range(4):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 6 ,2): # четные цифры
    print(i)

for i in 'qwerty':
    print(i)