# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import shutil
import sys
import easy

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл/директорию")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.makedirs(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.abspath(dir_name)
    try:
        os.chdir(dir_path)
        print(f'текущая директория: {dir_path}')
    except FileNotFoundError:
        print('не найдено')


def remove_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.abspath(dir_name)
    if os.path.isdir(dir_path):
        action = os.rmdir
    else:
        action = os.remove

    try:
        action(dir_path)
        print(f'{dir_path} удалено')
    except FileNotFoundError:
        print('не найдено')

    except OSError as ex:
        print(ex.args)


def show_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = os.path.abspath(dir_name)
    print(dir_path)

    try:
        list_dir = os.listdir(dir_path)
        dirs = []
        for item in list_dir:
            if os.path.isdir(os.path.join(dir_path, item)):
                dirs.append(item)
        files = []
        for item in list_dir:
            if os.path.isfile(os.path.join(dir_path, item)):
                files.append(item)
        for item in dirs:
            print(f'[{item}]')
        for item in files:
            print(item)

    except FileNotFoundError:
        print('не найдено')


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    src = os.path.abspath(dir_name)
    splitted_path = os.path.split(src)
    splitted_name = os.path.splitext(splitted_path[-1])
    print(splitted_name)

    try:
        new_file = shutil.copy(src, os.path.join(splitted_path[0], f'{splitted_name[0]}_copy{splitted_name[1]}'))

    except OSError as ex:
        print(ex.args)

    else:
        print(f'{new_file} создан')


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cd': change_dir,
    'rm': remove_dir,
    'ls': show_dir,
    'cp': copy_file,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        do['help']()
else:
    do['help']()
