# В файле храняться числа, нужно выбрать четные и составить список пар (число; квадрат числа).

path = 'c:/Users/5/OneDrive/GeekBrains/четверть 2/Знакомстао с языком Python/lesson_P/les18.py'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)

