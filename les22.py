# Функция enumerate
# функция enumerate() применяется к итерируемому объекту и
# возврощает новый итератор с кортежами из индекса и элементов входных данных.

users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users))
print(data)

