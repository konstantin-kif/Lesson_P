# Строки
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)

import numbers


text = 'съешь ещё этих мягких французских булок'

help(text.istitle)

# списки

numbers = [1,2,3,4]
print(numbers)

ran = range(1,6)
numbers = list(ran)
print(numbers)

numbers[0] = 10
print(numbers)

for i in numbers:
    i *= 2
    print(i)
print(numbers)