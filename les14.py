# Множества - уникальные элементы

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
print(colors)
colors.add('gray') # добовляем
print(colors)
colors.remove('red') # удояем
print(colors)
colors.discard('red') # удояем
print(colors)
colors.clear() # очистить
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # копия множества а 
u = a.union(b) # объеденение множества а с b
i = a.intersection(b) # перечечении множеств

s = frozenset(a) #  неизменяеммые множества (заморозка)