# Файлы
# Как работать с файлом, определиф модификатор работы
# a - открытие для добовления данных
# r - открытиие для чтения
# w - открытие для записи данных
# w+, r+

#with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')

#colors = ['red', 'green', 'blue']
#data = open('file.txt', 'a')
#data.writelines(colors) # разделителей не будет
#data.write('LINE 121\n') # \n переход на другую строку
#data.write('LINE 131\n')
#data.close() # разрываем связь

path = 'fale.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()