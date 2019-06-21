# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП,
# пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла

# Петр    Алексеев     22000          прораб          140


class Worker:
    def __init__(self, *args):
        args = args[0]
        self.name = args[0]
        self.surname = args[1]
        self.salary = args[2] if not args[2].isnumeric() else int(args[2])
        self.rank = args[3]
        self.norm = args[4] if not args[4].isnumeric() else int(args[4])
        self.worked_hours = 0

    def __str__(self):
        return f'{self.name} {self.surname} {self.rank}'

    def set_worked_hours(self, hours):
        self.worked_hours = hours

    def get_salary(self):
        if not str(self.norm).isnumeric():
            return 'Зарплата за месяц'

        if self.worked_hours <= self.norm:
            payment = self.salary * self.worked_hours / self.norm
        else:
            payment = self.salary + (self.salary / self.norm) * 2 * (self.worked_hours - self.norm)

        return round(payment, 2)


def parse_workers():
    with open('data/workers', encoding='UTF8') as f:
        workers = []
        for line in f.readlines():
            dataset = line.replace('\n', '').split(' ')
            dataset = list(filter(lambda x: x != '' and x != ' ', dataset))
            workers.append(Worker(dataset))

    return workers


def set_worked_hours():
    with open('data/hours_of', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            dataset = line.replace('\n', '').split(' ')
            dataset = list(filter(lambda x: x != '' and x != ' ', dataset))
            for worker in workers:
                if dataset[0] == worker.name and dataset[1] == worker.surname:
                    worker.set_worked_hours(dataset[2] if not dataset[2].isnumeric() else int(dataset[2]))


workers = parse_workers()
set_worked_hours()
for i in workers:
    print(f'{i.name:<10} {i.surname:<10} {i.salary:<10} {i.norm:<10} {i.worked_hours:<10} {i.get_salary():<10}')
