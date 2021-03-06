# Программа, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная objects, которая ссылается на список,
# содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.

objects = [1, 2, 1, 2, 3, 4, 4]

# Через создание множества с id.
s = set()
for obj in objects:
    s.add(id(obj))
print(len(s))


# Через создание нового списка.
final_list  = []
for obj in objects:
    if obj not in final_list:
        final_list.append(obj)
print(len(final_list))
