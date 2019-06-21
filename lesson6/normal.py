# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.


class Grade:
    def __init__(self, num, letter):
        self.num = num
        self.letter = letter

    def __str__(self):
        return f'{self.num}{self.letter}'


class Person:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'


class Student(Person):
    def __init__(self, surname, name, grade, parents):
        Person.__init__(self, surname, name)
        self.grade = grade
        self.parents = parents


class Parents:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'отец: {self.father}, мать: {self.mother}'


class Teacher(Person):
    def __init__(self, surname, name, discipline, grades):
        Person.__init__(self, surname, name)
        self.discipline = discipline
        self.grades = grades


discipline = ['JS',
              'HTML+CSS',
              'Django',
              'Agile',
              'Python'
              ]

grade = [Grade(5, 'А'),  # 0
         Grade(6, 'А'),  # 1
         Grade(7, 'Б'),  # 2
         Grade(7, 'А'),  # 3
         Grade(7, 'В'),  # 4
         Grade(6, 'Б'),  # 5
         Grade(8, 'А'),  # 6
         Grade(9, 'А'),  # 7
         ]

parents = [Parents('Иванов Иван', 'Иванова Мария'),  # 0
           Parents('Петров Пётр', 'Петрова Елена'),  # 1
           Parents('Сидоров Николай', 'Сидорова Татьяна'),  # 2
           Parents('Поляков Михаил', 'Полякова Ольга'),  # 3
           Parents('Семёнов Дмитрий', 'Семёнова Ольга'),  # 4
           Parents('Дрябезгов Константин', 'Дрябезгова Марина'),  # 5
           Parents('Шитов Денис', 'Шитова Наталья'),  # 6
           Parents('Жуков Юрий', 'Жукова Светлана'),  # 7
           Parents('Тимофеев Сергей', 'Тимофеева Наталья'),  # 8
           ]

students = [Student('Иванов', 'Сергей', grade[0], parents[0]),
            Student('Иванова', 'Екатерина', grade[0], parents[0]),
            Student('Петров', 'Иван', grade[0], parents[1]),
            Student('Петров', 'Кирилл', grade[1], parents[1]),
            Student('Сидоров', 'Алексей', grade[1], parents[2]),
            Student('Сидорова', 'Евгения', grade[3], parents[2]),
            Student('Поляков', 'Евгений', grade[3], parents[3]),
            Student('Полякова', 'Ольга', grade[4], parents[3]),
            Student('Семёнова', 'Екатерина', grade[4], parents[4]),
            Student('Семёнов', 'Андрей', grade[4], parents[4]),
            Student('Дрябезгов', 'Семён', grade[6], parents[5]),
            Student('Дрябезгов', 'Андрей', grade[6], parents[5]),
            Student('Шитов', 'Демид', grade[6], parents[6]),
            Student('Шитов', 'Меланья', grade[6], parents[6]),
            Student('Шитов', 'Роман', grade[6], parents[6]),
            Student('Жуков', 'Алексей', grade[5], parents[7]),
            Student('Жуков', 'Егор', grade[5], parents[7]),
            Student('Жуков', 'Никита', grade[5], parents[7]),
            Student('Жукова', 'Елена', grade[5], parents[7]),
            Student('Тимофеева', 'Наталья', grade[2], parents[8]),
            Student('Тимофеев', 'Сергей', grade[2], parents[8]),
            Student('Тимофеев', 'Пётр', grade[2], parents[8]),
            Student('Тимофеев', 'Анатолий', grade[2], parents[8]),
            Student('Тимофеева', 'Елена', grade[2], parents[8]),
            ]

teachers = [Teacher('Тарасов', 'Павел', discipline[0], (grade[0], grade[1], grade[4])),
            Teacher('Кадочников', 'Алексей', discipline[1], (grade[0], grade[1], grade[4], grade[2])),
            Teacher('Майков', 'Павел', discipline[2], (grade[0], grade[1], grade[4])),
            Teacher('Доу', 'Джон', discipline[3], (grade[5], grade[6], grade[7])),
            Teacher('Майков', 'Павел', discipline[4], (grade[5], grade[3], grade[2])),
            ]


def get_student_by_name(surname, name):
    student = None
    for stud in students:
        if stud.surname == surname and stud.name == name:
            student = stud
            break

    return student


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
def print_classes():
    print('Классы в школе')
    for item in grade:
        print(item)


# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")

def get_students_by_grade(grade_num, grade_letter):
    print(f'Ученики {grade_num}{grade_letter} класса:')
    for stud in students:
        if stud.grade.num == grade_num and f'{stud.grade.letter}'.upper() == grade_letter.upper():
            print(stud)


# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --

def get_disciples_by_student(surname, name):
    student = get_student_by_name(surname, name)

    if not student:
        print('Нет такого ученика')
        return

    st_teachers = []
    for teacher in teachers:
        if student.grade in teacher.grades:
            st_teachers.append(teacher)

    print(f'Дисциплины ученика {surname} {name}')
    for item in st_teachers:
        print(item.discipline)


# 4. Узнать ФИО родителей указанного ученика

def get_parents_by_student(surname, name):
    print(f'ученик {surname} {name}')
    student = get_student_by_name(surname, name)

    if not student:
        print('Нет такого ученика')
        return

    print(student.parents)


# 5. Получить список всех Учителей, преподающих в указанном классе

def get_teacher_by_grade(num, letter):
    st_grade = None
    for item in grade:
        if item.num == num and str(item.letter).upper() == letter.upper():
            st_grade = item
            print(st_grade)
            break

    if not st_grade:
        print('нет такого класса в школе')
        return

    st_teachers = []
    for teacher in teachers:
        if st_grade in teacher.grades:
            st_teachers.append(teacher)

    for i in st_teachers:
        print(i)


if __name__ == '__main__':
    # print_classes()

    # get_students_by_grade(5, 'А')

    # get_disciples_by_student('Шитов', 'Демид')
    # get_disciples_by_student('Жуков', 'Егор')

    # get_parents_by_student('Шитов', 'Демид')

    # get_teacher_by_grade(7, 'а')
    pass
