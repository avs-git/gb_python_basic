# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def split_fraction(fraction):
    """ возвращает переданную строку в виде неправильной дробь """
    if ' ' in fraction:
        temp = fraction.split(' ')
        total = int(temp[0])
        numenator = int(temp[1].split('/')[0])
        denominator = int(temp[1].split('/')[1])
        numenator = (denominator * abs(total) + numenator) * total / abs(total)

        return {'num': numenator, 'denum': denominator}

    if '/' in fraction:
        temp = fraction.split('/')
        numenator = int(temp[0])
        denominator = int(temp[1])
        return {'num': numenator, 'denum': denominator}

    else:
        return {'num': int(fraction), 'denum': 1}


def get_gcd(a, b):
    """ Возвращает наибольший общий знаменатель """
    a, b = abs(a), abs(b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return abs(a) or abs(b)


def calc_fraction_expression(string):
    print(string)
    items = string.split(' ')
    action = ''

    for item in items:
        if not item.isnumeric() and len(item) == 1:
            action = item

    side = string.split(f' {action} ')
    left = split_fraction(side[0])
    right = split_fraction(side[1])

    common_denum = left['denum'] * right['denum']
    left['num'] *= right['denum']
    right['num'] *= left['denum']
    print(f"{left['num']}/{common_denum} {action} {right['num']}/{common_denum}")
    if action == '+':
        result_num = left['num'] + right['num']

    elif action == '-':
        result_num = left['num'] - right['num']

    else:
        return f'{action} - непонятное действие'

    print(f'{result_num}/{common_denum}')

    gcd = get_gcd(result_num, common_denum)

    result_num = int(result_num / gcd)
    common_denum = int(common_denum / gcd)
    print(f'общий знаменатель: {gcd}')

    if abs(result_num) > common_denum:
        total = result_num // common_denum
        num = result_num % common_denum

    elif abs(result_num) < common_denum:
        total = ''
        num = result_num

    else:
        total = result_num / common_denum
        num, common_denum = '', ''

    fraction = ''
    if num:
        fraction = f'{num}/{common_denum}'

    return f'{total} {fraction}'

print(f'{"*" * 15} Задание1 {"*" * 15}')

print('ответ: ', calc_fraction_expression('5/6 + 4/7'))
print('ответ: ', calc_fraction_expression('-2/3 - -2'))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def get_workers():
    with open('data/workers', encoding='UTF-8') as f:
        workers = []
        for i, line in enumerate(f.readlines()):
            dataset = line.split(' ')
            dataset = list(filter(lambda x: x != '' and x != ' ', dataset))
            workers.append({})
            workers[i]['name'] = dataset[0]
            workers[i]['surname'] = dataset[1]
            workers[i]['salary'] = dataset[2]
            workers[i]['state'] = dataset[3]
            workers[i]['norm'] = dataset[4].replace('\n', '')

        return workers


def get_worked_hours():
    with open('data/hours_of', encoding='UTF-8') as f:
        hours = []
        for i, line in enumerate(f.readlines()):
            dataset = line.split(' ')
            dataset = list(filter(lambda x: x != '' and x != ' ', dataset))
            hours.append({})
            hours[i]['name'] = dataset[0]
            hours[i]['surname'] = dataset[1]
            hours[i]['worked'] = dataset[2].replace('\n', '')

        return hours


def append_hours_to_workers():
    workers = get_workers()
    hours = get_worked_hours()
    for worker in workers:
        for hour in hours:
            if worker['name'] == hour['name'] and worker['surname'] == hour['surname']:
                worker['worked'] = hour['worked']

    return workers


def calc_salary():
    workers = append_hours_to_workers()

    for worker in (workers):
        if not worker['salary'].isnumeric():
            continue
        norm = float(worker['norm'])
        worked = float(worker['worked'])
        salary = float(worker['salary'])

        if worked <= norm:
            payment = salary * worked / norm
        else:
            payment = salary + (salary / norm) * 2 * (worked - norm)

        worker['payment'] = round(payment, 2)

    return workers


def get_salary_by_names():
    workers = calc_salary()
    result = []
    for i, worker in enumerate(workers):
        result.append({})
        result[i]['name'] = worker['name']
        result[i]['surname'] = worker['surname']
        result[i]['payment'] = worker['payment'] if 'payment' in worker else 'Зарплата'

    return result


print('\n' * 2)
print(f'{"*" * 15} Задание2 {"*" * 15}')

for i in get_salary_by_names():
    print(i)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


def put_fruits_to_files():
    with open('data/fruits.txt', encoding='UTF-8') as f:
        for fruit in f.readlines():
            if fruit[0].isalpha():
                with open(f'data/fruits_{fruit[0].capitalize()}.txt', 'a', encoding='UTF-8') as fruit_file:
                    fruit_file.write(fruit)

    print('фрукты разложены по файлам')


print('\n' * 2)
print(f'{"*" * 15} Задание3 {"*" * 15}')

put_fruits_to_files()

