
from collections import namedtuple

END = '\n\n'
INDENT = ' ' * 4


# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки
print('вывести имена всех учеников из списка с новой строки')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print('{}{}'.format(INDENT, name))

print(END)


# Задание 2
# Необходимо вывести имена всех учеников из списка,
# рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???


# Задание 3
# Необходимо вывести имена всех учеников из списка,
# рядом с именем вывести пол ученика
print('вывести имена всех учеников из списка, \
    рядом с именем вывести пол ученика')
GENDER_CATALOG = {False: 'Женский', True: 'Мужской'}
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
user = namedtuple('User', ['name', 'gender'])
users = [user(name, is_male[name]) for name in names]
for user in users:
    name = user.name
    gender_str = GENDER_CATALOG[user.gender]
    print(INDENT, end='')
    print('Имя: {:<10} Пол: {}'.format(name, gender_str))

print(END)

# Задание 4
# Даны группу учеников.
# Нужно вывести количество групп
# и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.
print('вывести количество групп и для каждой группы \
    – количество учеников в ней')
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
groups_cnt = len(groups)
print('Всего групп: {}'.format(groups_cnt))
for group_index, group_users in enumerate(groups):
    print(INDENT, end='')
    group_size = len(group_users)
    print('Количество учеников в группе №{} = {}'.format(
        group_index,
        group_size,
    ))


print(END)

# Задание 5
# Для каждой пары учеников нужно с новой строки
# перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

print('Для каждой пары учеников нужно с новой строки \
    перечислить учеников, которые в неё входят.')
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for group_index, group_users in enumerate(groups):
    group_str = ', '.join(group_users)
    print(INDENT, end='')
    print('Группа №{}: {}'.format(group_index, group_str))
