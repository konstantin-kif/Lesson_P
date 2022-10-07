# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1))

def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5)) #  5 обозначает сколько раз !!!!!

def new_string(symbol, count = 3): # 3 обозночает во сколько раз
    return symbol * count
print(new_string('!')) # !!!
print(new_string(4))   # 12

def concatanatio(* params ):
    res: str = ""
    for item in params:
        res += item
    return res
print (concatanatio('a', 's', 'd', 'w' ))
print (concatanatio('a', '1' ))  