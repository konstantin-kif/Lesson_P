# Управляющие конструкции: if, if-else
# if condition: (если условие)
#    operator 1
#    operator 2
#    .........
#    operator n
# else: (ещё)
#    operator n + 1
#    operator n + 2
#    .........
#    operator n + m

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# if condition 1: (если условие)
#    operator
# elif condition 2:
#    operator
# elif condition 3:
#    operator
# eise:
#    operator

username = input('Ввудите имя: ')
if username == 'Маша':
    print('Ура, это же МАша')
elif username == 'Марина':
    print('Я так ждал Вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)        
