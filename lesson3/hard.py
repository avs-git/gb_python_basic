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

# def parse_string(string):
#     items = string.split(' ')
#     for item in items:
#         if not item.isnumeric() and len(item) == 1:
#             action = item
#
#     print(action)
#
# parse_string('-2/3 - -2')



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


put_fruits_to_files()
