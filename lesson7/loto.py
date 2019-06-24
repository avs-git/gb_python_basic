"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card:
    def __init__(self, name, player_type='ai'):
        self.digits = self.fill_card()
        # создаём плоскую копию карты для быстрого поиска вхождения
        self.flat_line = [x for i in self.digits for x in i]
        self.left = 15
        self.player = name
        self.player_type = player_type

    @staticmethod
    def fill_card():
        digits = [[], [], [], [], [], [], [], [], [], []]

        # Заполняем все ячейки в карте по столбцам
        for i, line in enumerate(digits):
            while len(line) < 3:
                num = random.randint(i * 10 or 1, (i + 1) * 10 - 1)
                if num not in line:
                    line.append(num)
            # Упорядочиваем столбцы
            line.sort()

        # Транспорируем таблицу
        t_digits = [[x[m] for x in digits] for m in range(len(digits[0]))]

        # Убираем 5 случайных значений из строки
        for row in t_digits:
            i = 0
            while i < 5:
                ind = random.randint(0, len(row) - 1)
                if str(row[ind]).isnumeric():
                    row[ind] = ' '
                    i += 1

        return t_digits

    def check_barrel(self, num):

        # логика для бота
        if self.player_type == 'ai':
            for line in self.digits:
                if num in line:
                    line[line.index(num)] = 'X'
                    self.left -= 1

        # логика для живого игрока
        else:
            print(f'бочонок {num}')
            answer = input(f'{self.player}, вычёркиваем (y) или продолжаем (n)?: ')
            if answer.upper() in ('Y', 'YES') and num in self.flat_line:
                for line in self.digits:
                    if num in line:
                        line[line.index(num)] = 'X'
                        self.left -= 1

            if (answer.upper() in ('Y', 'YES') and num not in self.flat_line) or \
                    (answer.upper() not in ('Y', 'YES') and num in self.flat_line):
                return f'Игра окончена. Игрок {self.player} проиграл. Он ошибся с выбором.'

        if self.left == 0:
            return f'Игра окончена! Победил игрок {self.player}'

        return False

    def __str__(self):
        string = f'{self.player}\n'
        string += '-' * 51 + '\n'
        for row in self.digits:
            string += '|'
            for item in row:
                string += f'{item:^4}|'
            string += '\n' + '-' * 51 + '\n'

        return string


class Bag:
    def __init__(self):
        self.barrels = [_ for _ in range(1, 100)]

    def get_barrel(self):
        if len(self.barrels) > 0:
            barrel = random.choice(self.barrels)
            self.barrels.remove(barrel)
            return barrel

        else:
            return 0

    def count(self):
        return len(self.barrels)


def render(barrel, turns=1):
    print(f'Ход {turns}')
    print(f'Бочонков в мешке {bag.count()}')
    print(f'Достали бочонок с номером {barrel}\n')

    for player in players:
        print(player)


def init():
    print('игра ЛОТО')

    global bag
    bag = Bag()
    global players
    players = []

    num_humans = input('Введите количество игроков (0 для автоматической игры): ')

    if num_humans.isnumeric():
        for i in range(int(num_humans)):
            player_name = input(f'Введите имя игрока {i + 1}: ')
            players.append(Card(player_name, 'human'))

    else:
        print('Количество игроков должно быть числом')
        return False

    num_bots = input('Количество ботов: ')

    if num_bots.isnumeric():
        for i in range(int(num_bots)):
            players.append(Card(f'bot {i + 1}'))

    else:
        print('Количество ботов должно быть числом')
        return False

    if len(players) == 0:
        print('Некому играть. Расходимся')
        return False

    return True


def run():
    if init():

        turns = 1

        while True:
            barrel = bag.get_barrel()
            stop_event = False

            render(barrel, turns)
            for player in players:
                stop_event = player.check_barrel(barrel)
                if stop_event:
                    break

            if not stop_event:
                turns += 1

            else:
                print(f'{"*" * 10} РЕЗУЛЬТАТЫ ИГРЫ {"*" * 10}')
                render(barrel, turns)
                print(f'Игра закончилась на {turns} ходу')
                print(f'Осталось бочонков в мешке: {bag.count()}')
                print(stop_event)
                break


if __name__ == '__main__':
    run()
