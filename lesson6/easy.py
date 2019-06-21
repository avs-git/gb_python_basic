class Figure:
    def __init__(self, tops):
        self.tops = tops

    def get_side_lenght(self, a, b):
        return (abs(b[0] - a[0]) ** 2 + abs(b[1] - a[1]) ** 2) ** 0.5

    @property
    def sides(self):
        side = []
        for i in range(len(self.tops)):
            side.append(self.get_side_lenght(self.tops[i], self.tops[(i + 1) % len(self.tops)]))

        return side

    @property
    def perimeter(self):
        return sum(self.sides)


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle(Figure):
    def __init__(self, tops):
        Figure.__init__(self, tops)
        if len(tops) != 3:
            pass

    # возвращает список высот
    def high(self, high_num=None):
        if not -1 < high_num < 3:
            print('Введите верный номер вершины треугольника (0, 1, 2)')
            return False

        p = self.perimeter / 2
        h = []
        side = self.sides

        for i in side:
            h.append(round((2 * (p * (p - side[0]) * (p - side[1]) * (p - side[2])) ** 0.5) / i, 3))

        return h[high_num]

    @property
    def square(self):
        return round(self.sides[1] * self.high(1) / 2, 3)


tr_1 = Triangle(((0, 0), (0, 1), (2, 0)))
print(tr_1.tops)
print(tr_1.perimeter)
print(tr_1.high(2))
print(tr_1.square)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Figure):
    def __init__(self, tops):
        Figure.__init__(self, tops)

    def get_hor_lines(self):
        args = self.tops

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

        return line1, line2

    def is_right(self):
        line1, line2 = self.get_hor_lines()

        if line1[0][0] - line2[0][0] != line2[1][0] - line1[1][0] or line1[1][0] - line1[0][0] == 0:
            return False

        return True

    @property
    def square(self):
        line1, line2 = self.get_hor_lines()
        line = (line1[1][0] - line1[0][0], line2[1][0] - line2[0][0])

        arrY = [x[1] for x in self.tops]

        h = max(arrY) - min(arrY)

        return h * sum(line) / 2

    def get_sides_length(self):
        lines = list(self.get_hor_lines())
        lines.append([lines[0][0], lines[1][0]])
        lines.append([lines[1][1], lines[0][1]])
        line_len = []

        for i in lines:
            line_len.append(self.get_side_lenght(i[0], i[1]))

        return line_len


trap_1 = Trapezium(((1, 5), (3, 1), (5, 1), (7, 5)))
print(trap_1.is_right())
print(trap_1.perimeter)
print(trap_1.square)
print(trap_1.get_sides_length())
