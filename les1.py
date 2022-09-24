# Тип данных и переменная
# Int - целый числа, Float - числа с плавуещей точкой,
# boo lean - логическая переменная, str или list - буквы

from operator import truediv


value = None
a = 123 # числа
b = 1.23
print(a) # ввывод чисел
print(b)
value = 1234
print(value)
str = "Hello world" # строки
print(str)  # ввывод строк
print(a, b, str) # виды ввыводов
print(a, '-', b, '-', str)
print('{} - {} - {}'.format(a, b, str))
print(f'{a} - {b} - {str}')
print('{1} - {2} - {0}'.format(a, b, str))

t = True # Логическая переменная
f = False
print(t)
print(f)

list = [1, 2, 3, 'hello world'] # массив
print(list)