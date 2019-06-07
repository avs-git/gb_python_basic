def timer(function):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f'затраченое время: {time.time() - start_time}')
        return result

    return wrapper


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

@timer
def fibonacci(n, m):
    if n > m:
        n, m = m, n

    fibo = [1, 1]

    # m - 2 так как 2 первых элемента у нас уже есть.
    for i in range(m - 2):
        # sum не используем, так как сильно увеличивает время
        fibo.append(fibo[-1] + fibo[-2])

        # чистим массив ненужных элементов, даёт прирост при n > 1000. +1 элемент на случай для m == n
        if len(fibo) > m - n + 1:
            # pop выгодней, чем remove
            fibo.pop(0)

    # n < m, возвращаем конец массива без вспомогательных элементов, добавленных ранее
    return fibo[n - m - 1:]


print(fibonacci(500000, 500004))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\n' * 2)
print(f'{"*" * 15} Задание2 {"*" * 15}')


@timer
def sort_to_max(numlist):
    sorted_list = []

    for i in numlist:
        sorted_list.append(min(numlist))
        numlist.remove(min(numlist))

    return sorted_list

    # метод пузырька

    # passed = 0
    # steps = 0
    # while passed != len(numlist) - 1:
    #     passed = 0
    #
    #     for i in range(len(numlist) - 1):
    #         steps += 1
    #         if numlist[i] > numlist[i + 1]:
    #             numlist[i], numlist[i + 1] = numlist[i + 1], numlist[i]
    #             continue
    #         passed += 1

    # print(f'steps: {steps}')
    # return numlist


def make_test_arr(num):
    a = []
    from random import randint
    for i in range(num):
        a.append(randint(-100, 100))

    return a


some_arr = make_test_arr(2000)

print(sort_to_max(some_arr))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


print('\n' * 2)
print(f'{"*" * 15} Задание 3 {"*" * 15}')


def only_odd_filter(num):
    if not num % 2:
        return num


def custom_filter(func, iterable_item):
    result = []
    for i in iterable_item:
        if func(i):
            result.append(i)
    return result


print('original:')
print(list(filter(lambda x: x != ' ', 'а роза упала на лапу азора')))
print(list(filter(only_odd_filter, [1, 2, 3, 4, 5, 6])))

print('\ncustom:')
print(custom_filter(lambda x: x != ' ', 'а роза упала на лапу азора'))
print(custom_filter(only_odd_filter, [1, 2, 3, 4, 5, 6]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('\n' * 2)
print(f'{"*" * 15} Задание 4 {"*" * 15}')


# принимает точки в любой последовательности
# если все 4 точки на одной линии - False
# прямоугольник - тоже параллелограм
def is_parallelogram(*args):
    print(args)

    if len(args) != 4:
        return False

    arrY = list(map(lambda x: x[1], args))

    for i in args:
        if arrY.count(i[1]) != 2:
            return False

    line2 = list(args)
    line1 = [line2[0]]
    line2.pop(0)

    for i in line2:
        if line1[0][1] == i[1]:
            line1.append(i)
            line2.remove(i)

    line1 = sorted(line1)
    line2 = sorted(line2)

    if line1[1][0] - line1[0][0] != line2[1][0] - line2[0][0] or line1[1][0] - line1[0][0] == 0:
        return False

    return True


# равнобедренная трапеция
a1, a2, a3, a4 = (1, 5), (3, 1), (9, 5), (4, 1)
print(is_parallelogram(a1, a2, a3, a4))

# Параллелограмм
a1, a2, a3, a4 = (1, 5), (3, 1), (9, 5), (11, 1)
print(is_parallelogram(a1, a2, a3, a4))
