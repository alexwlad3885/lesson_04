# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = (200, "string", [1, 2, 3], (10, 20))
print(f'Immutable tuple: {immutable_var}')
# immutable_var[0] = 300  изменить значение объекта "кортеж" нельзя, т.к. он неизменяемый
immutable_var[2][1] = 8   # в элементе "список" можно изменить элементы, т.к. элементы списка изменяемые
print(f'Immutable tuple: {immutable_var}')
mutable_list = [10, 20, 30, 40]
mutable_list.append(50)     #добавляем новый элемент к списку
mutable_list[1] = 25        #меняем значение 2 элемента списка
print(f'Mutable list: {mutable_list}')


