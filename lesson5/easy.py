import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import re
import shutil
import sys


def is_filename_incorrect(name):
    if not name:
        print('Имя не может быть пустым')
        return True

    incorrect_symbols = ':*?<>|'
    for char in incorrect_symbols:
        if char in name:
            print(f'неправильное имя файла или директории. Имя не может содержать {incorrect_symbols}')
            return True


def make_dir_custom(dir_name=None):
    if not dir_name:
        dir_name = input('Введите название папки: ')

    if is_filename_incorrect(dir_name):
        return False

    try:
        os.makedirs(dir_name)

    except FileExistsError:
        print(f'{dir_name} - директория существует')

    else:
        print(f'{dir_name} - директория создана')


def remove_dir_custom(dir_name=None):
    if not dir_name:
        dir_name = input('Введите название папки: ')

    if is_filename_incorrect(dir_name):
        return False

    try:
        os.rmdir(dir_name)

    except FileExistsError:
        print('Файлы не найдены')

    except PermissionError:
        print('отказано в доступе')

    except FileNotFoundError:
        print('Файл не найден')

    except NotADirectoryError:
        print('Указанное имя - не директория')

    except Exception:
        print(f'Some another shit happened')

    else:
        print(f'директория {dir_name} удалена')


def make_number_dirs(dir_name=None, number=1):
    if not dir_name:
        dir_name = input('Введите название папки: ')
        number = int(input('Введите количество дублей: '))

    if is_filename_incorrect(dir_name):
        return False

    for i in range(number):
        make_dir_custom(f'{dir_name}_{i + 1}')


# make_number_dirs(input('Введите имя директории: '), 9)

def get_same_names(name):
    file_list = ','.join(os.listdir(os.getcwd()))
    return re.findall(name + r'_\d+', file_list)


def remove_number_dirs(dir_name=None):
    if not dir_name:
        dir_name = input('Введите название папки: ')

    list_to_remove = get_same_names(dir_name)

    if list_to_remove:
        answer = input(f'Директории:\n {list_to_remove} будут удалены.\nПродолжить? y/n: ')
        if answer == 'y':
            for file in list_to_remove:
                remove_dir_custom(file)

        else:
            print('Отмена')
            return False

    else:
        print(f'не найдено директорий {dir_name}_#')
        return False


# remove_number_dirs(input('Введите имя директории: '))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def ls():
    list_dir = os.listdir(os.getcwd())
    print(f'{os.getcwd()}:')
    dirs = [item for item in list_dir if os.path.isdir(item)]
    files = [item for item in list_dir if os.path.isfile(item)]
    print('..')
    for item in dirs:
        print(f'[{item}]')
    for item in files:
        print(item)


def cd(dir_name=None):
    if not dir_name:
        dir_name = input('Введите папку назначения: ')

    if is_filename_incorrect(dir_name):
        print('неверное имя директории')
        return False

    try:
        os.chdir(dir_name)

    except PermissionError:
        print('Нет прав доступа')

    except FileNotFoundError:
        print('не существует')

    else:
        print(os.getcwd())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(filename):
    os.getcwd()

def copy_me():
    this = sys.argv[0]
    this_name = this.split('/')[-1].split('.')[-2]
    this_extension = this.split('/')[-1].split('.')[-1]

    num = len(get_same_names(this_name)) + 1
    try:
        new_name = shutil.copy(f'{this_name}.{this_extension}', f'{this_name}_{num}.{this_extension}')

    except PermissionError:
        print('отказано в доступе')

    else:
        print(f'файл {new_name} создан')


if __name__ == '__main__':
    copy_me()
    ls()
