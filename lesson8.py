# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#    В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
#    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#    Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        self.str_date = str_date
        self.day = self.str_date[0]
        self.mounth = self.str_date[1]
        self.year = self.str_date[2]
        print(f'{self.day}-{self.mounth}-{self.year}')

    @classmethod
    def num_date(cls, str_date):
        num_date = list(map(int, str_date.split('-')))
        return cls(num_date)

    @staticmethod
    def date_valid(obj):
        obj = list(map(int, obj.split('-')))
        if obj[0] in range(1, 31) and obj[1] in range(1, 12):
            return 'Всё верно'
        elif obj[0] not in range(1, 31):
            return 'Число должно быть в диапазоне от 1 до 31'
        elif obj[1] not in range(1, 12):
            return 'Месяц должен быть в диапазоне от 1 до 12'

Date.num_date('10-02-2003')
print(Date.date_valid('10-02-2003'))
Date.num_date('25-12-2010')
Date.num_date('35-05-1990')
print(Date.date_valid('35-05-1990'))
Date.num_date('04-15-2000')
print(Date.date_valid('04-15-2000'))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#    Проверьте его работу на данных, вводимых пользователем.
#    При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Div_by_zero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    math_equation = input('Введите уравнение: ').split()
    if math_equation[2] == '0':
        raise Div_by_zero('Деление на 0 запрещено')
except Div_by_zero as err:
    print(err)
else:
    math_equation = int(math_equation[0]) / int(math_equation[2])
    print(math_equation)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#    Проверить работу исключения на реальном примере.
#    Запрашивать у пользователя данные и заполнять список необходимо только числами.
#    Класс-исключение должен контролировать типы данных элементов списка.
#    Примечание: длина списка не фиксирована.
#    Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
#    При этом скрипт завершается, сформированный список с числами выводится на экран.
#    Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
#    Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
#    Вносить его в список, только если введено число.
#    Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
#    При этом работа скрипта не должна завершаться.

class Only_numbers(Exception):
    def __init__(self, text):
        self.text = text

try:
    num_list = []
    while True:
        data = input('Введите числа: ')
        if data == 'stop':
            break
        elif data.isdigit():
            num_list.append(data)
        else:
            print(Only_numbers('Введено не число'))
            continue
except Only_numbers as err:
    print(err)
else:
    print(num_list)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#    А также класс «Оргтехника», который будет базовым для классов-наследников.
#    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определите параметры, общие для приведённых типов.
#    В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
#    Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
#    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#    можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
#    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#    Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod

class Input_validation(Exception):
    def __init__(self, txt):
        self.txt = txt

class Office_equipment_warehouse:
    reception = {}
    transfer = {}
    def reception_of_equipment(self, eqipment_name, equipment_count):
        self.eqipment_name = eqipment_name
        self.equipment_count = equipment_count
        try:
            if self.equipment_count.isdigit():
                self.reception[self.eqipment_name] = self.equipment_count
            else:
                raise Input_validation('Введите количество цифрами')
        except Input_validation as err:
            print(err)

    def transfer_of_equipment(self, eqipment_name, equipment_count):
        self.eqipment_name = eqipment_name
        self.equipment_count = equipment_count
        try:
            if self.equipment_count.isdigit():
                self.transfer[self.eqipment_name] = self.equipment_count
            else:
                raise Input_validation('Введите количество цифрами')
        except Input_validation as err:
            print(err)

class Office_equipment(ABC):
    @abstractmethod
    def get_source_doc(self, process):
        self.process = process
        print(f'Исходный документ получен на {self.process}')

    @abstractmethod
    def start(self, equipment_name):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} начал работу')

    @abstractmethod
    def result(self, equipment_name):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} завершил работу')

class Printer(Office_equipment):
    def get_source_doc(self, process = 'печать'):
        self.process = process
        print(f'Исходный документ получен на {self.process}')

    def start(self, equipment_name = 'Принтер'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} начал работу')

    def doc_print(self):
        print('Печать документа произведена')

    def result(self, equipment_name = 'Принтер'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} завершил работу')

class Scanner(Office_equipment):
    def get_source_doc(self, process = 'сканирование'):
        self.process = process
        print(f'Исходный документ получен на {self.process}')

    def start(self, equipment_name = 'Сканер'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} начал работу')

    def doc_scan(self):
        print('Документ отсканирован')

    def result(self, equipment_name = 'Сканер'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} завершил работу')

class Xerox(Office_equipment):
    def get_source_doc(self, process = 'ксерокопирование'):
        self.process = process
        print(f'Исходный документ получен на {self.process}')

    def start(self, equipment_name = 'Ксерокс'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} начал работу')

    def doc_xerox(self):
        print('Ксерокопия документа выполнена')

    def result(self, equipment_name = 'Ксерокс'):
        self.eqipment_name = equipment_name
        print(f'{self.eqipment_name} завершил работу')

first_document = Printer()
first_document.get_source_doc()
first_document.start()
first_document.doc_print()
first_document.result()
print('')
second_document = Scanner()
second_document.get_source_doc()
second_document.start()
second_document.doc_scan()
second_document.result()
print('')
third_document = Xerox()
third_document.get_source_doc()
third_document.start()
third_document.doc_xerox()
third_document.result()

print('')
a = Office_equipment_warehouse()

a.reception_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
a.reception_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
a.reception_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
print('Принятая оргтехника:')
print(a.reception)
print('')
a.transfer_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
a.transfer_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
a.transfer_of_equipment(input('Введите наименование оборудования: '), input('Введите количество оборудования: '))
print('Переданная оргтехника:')
print(a.transfer)

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
#    Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
#    Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
#    Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        self.complex_num = complex(real_part, imaginary_part)
        print(self.complex_num)

    def __add__(self, other):
        return f'{complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)}'

    def __mul__(self, other):
        return complex(self.real_part, self.imaginary_part) * complex(other.real_part, other.imaginary_part)

print('Первое комплексное число: ')
a = Complex_number(1, 2)
print('Второе комплексное число: ')
b = Complex_number(3, 4)
print('Сумма комплексных чисел:')
print(a + b)
print('Произведение комплексных чисел:')
print(a * b)