# input() - отвечает зв ввод данных
# print() - отвечает за вывод данных

print('Введите a')
a = input()
print('Введите b')
b = input()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

print('Введите a')
a = int(input()) # целые числа
print('Введите b')
b = int(input())
print(a, ' + ', b, ' = ', a + b)

print('Введите a')
a = float(input()) # числа с плавуещей точкой
print('Введите b')
b = float(input())
print(a, ' + ', b, ' = ', a + b)