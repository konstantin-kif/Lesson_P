# Логические операции
# >,>=,<,<=,==,!=
# not,and,or-не путать с &,|,^
# Кое-что ещё: is,is not,in,not in

a = 1 > 4
print(a)
a = 1 < 4
print(a)
a = 1 < 4 and 5 > 2
print(a)
a = 1 == 2
print(a)
a = 1 != 2
print(a)
a = 'qwe'
b = 'qwe'
print(a == b)
a = [1,2]
b = [2,1]
print(a == b)
a = 1 < 3 < 5
print(a)

func = 1
T = 4
x = 2
print(func<T>(x)) # тройное неравенство

f = 1 > 2 or 4 < 6 # Одна из формул истина значит будет истина
print(f)

f = [1,2,3,4]
print(f)
print(not 2 in f)

is_odd = f[0] % 2 
print(is_odd)