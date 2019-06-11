# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
from random import randint

matrix = [[1, 0, 8, 5],
          [3, 4, 1, 6],
          [0, 4, 2, 8]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix_t = [[x[m] for x in matrix] for m in range(len(matrix[0]))]
print(matrix_t)


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.


def get_mult(elem_list):
    mult = 1
    for i in elem_list:
        mult *= i
    return mult


num_size = 1000
test_pack_size = 5

number = ''
for i in range(1000):
    number += str(randint(0, 9))

max_mult = 0
position = 0
for i in range(len(number) - test_pack_size):
    test_pack = [int(x) for x in number[i: i + test_pack_size]]
    test_mult = get_mult(test_pack)
    if test_mult > max_mult:
        max_mult = test_mult
        position = i

print(f'позиция: {position}, произведение: {max_mult}')

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

coords = ((1, 2),
          (2, 3),
          (4, 5),
          (5, 8),
          (8, 1),
          (6, 5),
          (7, 4),
          (3, 3)
          )

x = [i[0] for i in coords]
y = [i[1] for i in coords]


def check_standing(x, y):
    if len(set(x)) != len(x) or len(set(y)) != len(y):
        return False

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if abs(x[i] - x[j]) == abs(x[i] - y[1]):
                return False

    return True


print('NO' if check_standing(x, y) else 'YES')
