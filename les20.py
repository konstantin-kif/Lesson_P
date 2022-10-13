# Функция Filter
# Функция Filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых функция вернула True.

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2 , data))
print(res)

ata = '1 2 3 4 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)