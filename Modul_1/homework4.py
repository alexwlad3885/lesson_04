# Практическая работа по уроку "Организация программ и методы строк."
my_string = input('Введите любой текст: ')
print("длина текста ", str(len(my_string)), ' символов')
print(my_string.upper())                        # верхний регистр
print(my_string.lower())                        # нижний регистр
print(my_string.replace(' ', ''))   # убирает пробелы
print(my_string[0])                             # первый символ
print(my_string[len(my_string)-1])              # последний символ
