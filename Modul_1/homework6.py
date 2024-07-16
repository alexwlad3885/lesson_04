# Практическое задание по теме: "Словари и множества"

# Работа со словарями:
my_dict = {"Vasya": 1975, "Egor": 1999, "Masha": 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["Egor"]}')
print(f'Not existing value: {my_dict.get("Dima")}')
my_dict.update(Sergey=2003, Lena=2006)
value = my_dict.pop("Egor")
print(f'Deleted value: {value}')
print(f'Modified dictionary: {my_dict}\n')

# Работа с множествами:
my_set = {1, 2, 3, 4, 5, 2, 4, 8, 1, "Nicholas", "Michelle", 42.314, "Nicholas"}
print(f'Set: {my_set}')
my_set.add((2, 13, 5.2))
my_set.add(13)
my_set.discard(8)
print(f'Modified set: {my_set}')
