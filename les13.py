# Словари - это неупарядоченные коллекции
# поизвольных объектов с доступом по ключу 

dictionary = {}   # {} - обозначает пустой словарь
dictionary = \
    {
        'up': '+',        # присвоение обозначение к ключу
        'left': '+-',
        'down': '-',
        'right': '-+' 
    }
print(dictionary)
print(dictionary['left'])

# Типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:
    print(v)
    
for v in dictionary:
    print(dictionary[v])