# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#    который должен принимать данные (список списков) для формирования матрицы.
#    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#    Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#    31    32         3    5    32        3    5    8    3
#    37    43         2    4    6         8    3    7    1
#    51    86        -1   64   -8
#
#    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
#    Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#    Подсказка: сложение элементов матриц выполнять поэлементно —
#    первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_print = ''
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                if i > 0 and j == 0:
                    matrix_print += '\n' + ''.join(str(self.matrix_list[i][j])) + '\t'
                else:
                    matrix_print += ''.join(str(self.matrix_list[i][j])) + '\t'
        return matrix_print

    def __add__(self, other):
        new_matrix = self.matrix_list
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[i])):
                new_matrix[i][j] += other.matrix_list[i][j]
        return Matrix(new_matrix)

matrix1 = Matrix([[31, 32], [37, 43], [51, 86]])
print('Первая матрица:')
print(matrix1)
print('')
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print('Вторая матрица:')
print(matrix2)
print('')
matrix3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print('Третья матрица:')
print(matrix3)
print('')
matrix4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Четвертая матрица:')
print(matrix4)
print('')
matrix5 = Matrix([[7, 8, 9], [11, 12, 13], [14, 15, 16]])
print('Пятая матрица:')
print(matrix5)
print('')
print('Сумма четвёртой и пятой матриц:')
print(matrix4 + matrix5)


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#    Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
#    К типам одежды в этом проекте относятся пальто и костюм.
#    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#    Это могут быть обычные числа: V и H, соответственно.
#    Для определения расхода ткани по каждому типу одежды использовать формулы:
#    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#    Реализовать общий подсчет расхода ткани.
#    Проверить на практике полученные на этом уроке знания:
#    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Outerwear(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Outerwear):
    def fabric_consumption(self, V):
        self.V = V
        fabric_for_coat = (self.V / 6.5 + 0.5)
        return fabric_for_coat

class Suit(Outerwear):
    def fabric_consumption(self, H):
        self.H = H
        fabric_for_suit = (2 * self.H + 0.3)
        return fabric_for_suit

class Fabric(Outerwear):
    def fabric_consumption(self, V, H):
        self.V = V
        self.H = H
        total_fabric_consumption = Coat.fabric_consumption(self, V) + Suit.fabric_consumption(self, H)
        return total_fabric_consumption

print('Расход ткани на пальто:')
finished_coat = Coat()
print('%.3f' % finished_coat.fabric_consumption(42))
print('Расход ткани на костюм:')
finished_suit = Suit()
print('%.3f' % finished_suit.fabric_consumption(170))
print('Общий расход ткани:')
total_consumption = Fabric()
print('%.3f' % total_consumption.fabric_consumption(42, 170))


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
#    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
#    В классе должны быть реализованы методы перегрузки арифметических операторов:
#    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
#    и целочисленное (с округлением до целого) деление клеток, соответственно.
#
#    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
#    Данный метод позволяет организовать ячейки по рядам.
#    Метод должен возвращать строку вида *****\n*****\n*****...,
#    где количество ячеек между \n равно переданному аргументу.
#    Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
#    Тогда метод make_order() вернёт строку: *****\n*****\n**.
#    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
#    Тогда метод make_order() вернёт строку: *****\n*****\n*****.
#    Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        return self.cells_count + other.cells_count

    def __sub__(self, other):
        if self.cells_count - other.cells_count > 0:
            return self.cells_count - other.cells_count
        else:
            return 'Разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        return Cell(self.cells_count // other.cells_count)

    def __str__(self):
        return f'{self.cells_count}'

    def make_order(self, row_cells_count):
        self.row_cells_count = row_cells_count
        res_row = ''
        for i in range(self.cells_count // self.row_cells_count):
            for j in range(self.row_cells_count):
                res_row += '*'
            res_row += '\n'
        if self.cells_count % self.row_cells_count != 0:
            res_row += '*' * (self.cells_count % self.row_cells_count)
        return res_row

first_cell = Cell(5)
second_cell = Cell(3)
print('Сложение:', first_cell + second_cell)
print('Вычитание:', first_cell - second_cell)
print('Умножение:', first_cell * second_cell)
print('Деление:', first_cell / second_cell)
third_cell = Cell(12)
print(third_cell.make_order(5))
