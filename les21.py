# Функция zip() применяется к набору итерируемых объектов и возврощает итератор
# c кортежами из элементов данных.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333,]

data = list(zip(users, ids, salary))
print(data)
