
from collections import Counter

END = '\n\n'
INDENT = ' ' * 4

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('посчитать количество повторений каждого имени ученика')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

student_names = [student['first_name'] for student in students]
names_counter = Counter(student_names)
name_cnts = dict(names_counter)
for name, cnt in name_cnts.items():
    print(INDENT, end='')
    print('{}: {}'.format(name, cnt))

print(END)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# Пример вывода:
# Самое частое имя среди учеников: Маша

print('нужно вывести самое часто повторящееся имя')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
most_common_name = names_counter.most_common(1)[0][0]
print(INDENT, end='')
print('самое часто повторящееся имя: {}'.format(most_common_name))


print(END)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print('нужно вывести самое частое имя в каждом классе')
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

def get_most_common_name(group):
    student_names = [users['first_name'] for users in group]
    names_counter = Counter(student_names)     
    return names_counter.most_common(1)[0][0]


for group_index, users in enumerate(school_students, 1):
    most_common_name = get_most_common_name(users)
    print(INDENT, end='')
    print('Самое частое имя в классе {}: {}'.format(group_index, most_common_name))


print(END)

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print('вывести количество девочек и мальчиков в нём')
school = [
    {
        'class': '2a',
        'students': [
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ],
    },
    {
        'class': '3c',
        'students': [
            {'first_name': 'Олег'},
            {'first_name': 'Миша'},
        ],
    },
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


# def flatten(nested):
    # for dict_ in nested:




# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a