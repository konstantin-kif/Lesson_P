# В файле храняться числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример 1 2 3 4 5 8 15 23 38
# path = 'c:/Users/5/OneDrive/GeekBrains/четверть 2/Знакомстао с языком Python/lesson_P/les18.py'
#f = open(path, 'r')
#data = f.read() + ' '
#f.close()

#numbers = []

#while data != '':
#    space_pos = data.index(' ')
#    numbers.append(int(data[:space_pos]))
#    data = data[space_pos+1:]

#out = []
#    if not e % 2:
#    out.append((e, e**2))
#print(out)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)

print(res)