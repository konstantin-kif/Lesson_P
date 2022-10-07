# Списки

from re import L


list1 = [1,2,3,4,5,]
list2 = list1

for e in list1:
    print(e)

print()
for e in list2:
    print(e)

list1 = [1,2,3,4,5,]

print(list1)
print(list1.pop()) # извлечение последнего элемента
print(list1)
print(list1.pop(2)) # указали какой масив надо удалить
print(list1)
print(list1.insert(2, 11)) # добовляем число в массив 
print(list1)
print(list1.append(22)) # добовляем число в  конец массива 
print(list1)