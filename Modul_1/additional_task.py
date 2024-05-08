students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#  переводим множество в список для упорядочивания элементов
neo_students = list(students)
#  сортируем список
neo_students.sort()
#  создаем пустой словарь
neo_students_ = dict()
# len(neo_students) количество элементов в списке
for a in range(len(neo_students)):
    neo_students_[neo_students[a]] = sum(grades[a]) / len(grades[a])
print(neo_students_)
