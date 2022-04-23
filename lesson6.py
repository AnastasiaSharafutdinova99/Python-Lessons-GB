# 1. Создать класс TrafficLight (светофор).
#    определить у него один атрибут color (цвет) и метод running (запуск);
#    атрибут реализовать как приватный;
#    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
#    третьего (зелёный) — на ваше усмотрение;
#    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#    проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов.
#    При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLigth:
    __color = ['Red', 'Yellow', 'Green']

    def runnig(self):
        color = TrafficLigth.__color
        for el in color:
            if el == 'Red':
                print('Красный')
                sleep(7)
            if el == 'Yellow':
                print('Жёлтый')
                sleep(2)
            if el == 'Green':
                print('Зелёный')
                sleep(5)

new_TrafficLigth = TrafficLigth()
new_TrafficLigth.runnig()


# 2. Реализовать класс Road (дорога).
#    определить атрибуты: length (длина), width (ширина);
#    значения атрибутов должны передаваться при создании экземпляра класса;
#    атрибуты сделать защищёнными;
#    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#    использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#    толщиной в 1 см*число см толщины полотна;
#    проверить работу метода.
#    Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight_calculate(self, asphaltW_per_sqrMeter, road_thickness):
        self.asphaltW_per_sqrMeter = asphaltW_per_sqrMeter
        self.road_thickness = road_thickness
        asphalt_weight = self._length * self._width * self.asphaltW_per_sqrMeter * self.road_thickness
        print(f'{self._length}м * {self._width}м * {self.asphaltW_per_sqrMeter}кг * {self.road_thickness}см = {asphalt_weight // 1000}т')

asphalt_for_road = Road(20, 5000)
asphalt_for_road.asphalt_weight_calculate(25, 5)


# 3. Реализовать базовый класс Worker (работник).
#    определить атрибуты: name, surname, position (должность), income (доход);
#    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#    оклад и премия, например, {"wage": wage, "bonus": bonus};
#    создать класс Position (должность) на базе класса Worker;
#    в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#    и дохода с учётом премии (get_total_income);
#    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#    проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print('Полное имя сотрудника: ' + self.name + ' ' + self.surname)

    def get_total_income(self):
        total_incom = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход с учетом премии: {total_incom}')

first_employee = Position('Василий', 'Иванов', 'Python разработчик', 100000, 50000)
first_employee.get_full_name()
first_employee.get_total_income()
print('')
second_employee = Position('Иван', 'Степанов', 'Архитектор баз данных', 120000, 60000)
second_employee.get_full_name()
second_employee.get_total_income()
print('')
third_employee = Position('Алина', 'Петрова', 'Бизнес аналитик', 70000, 35000)
third_employee.get_full_name()
third_employee.get_total_income()


# 4. Реализуйте базовый класс Car.
#    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    А также методы: go, stop, turn(direction), которые должны сообщать,
#    что машина поехала, остановилась, повернула (куда);
#    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
#    и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#    Вызовите методы и покажите результат.
#
class Car:
    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена допустимая скорость')
        else:
            self.speed = Car.show_speed(self)

class SportCar(Car):
    def drift(self):
        print (f'{self.name} дрифтует')

class WorkCar(Car):
    def working(self):
        print(f'{self.name} убирает снег')

    def show_speed(self):
        if self.speed > 40:
            print('Превышена допустимая скорость')
        else:
            self.speed = Car.show_speed(self)

class PoliceCar(Car):
    def patrol(self):
        print(f'{self.name} патрулирует улицы')

base_car = Car(50, 'Audi', 'Синий', False)
base_car.go()
base_car.stop()
base_car.turn('направо')
base_car.show_speed()
print(base_car.is_police)
print('')
first_car = TownCar(65, 'Skoda', 'Белый', False)
first_car.go()
first_car.show_speed()
first_car.stop()
print(first_car.is_police)
print('')
second_car = SportCar(90, 'Nissan', 'Чёрный', False)
second_car.go()
second_car.turn('направо')
second_car.show_speed()
second_car.drift()
print(second_car.is_police)
print('')
third_car = WorkCar(30, 'Cat', 'Оранжевый', False)
third_car.go()
third_car.turn('налево')
third_car.show_speed()
third_car.working()
print(third_car.is_police)
print('')
fourth_car = PoliceCar(60, 'Toyota', 'Белый', True)
fourth_car.go()
fourth_car.turn('направо')
fourth_car.show_speed()
fourth_car.patrol()
print(fourth_car.is_police)


# 5. Реализовать класс Stationery (канцелярская принадлежность).
#    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#    в каждом классе реализовать переопределение метода draw.
#    Для каждого класса метод должен выводить уникальное сообщение;
#    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        self.title = 'Запуск отрисовки'
        print(self.title)

class Pen(Stationery):
    def draw(self):
        # self.title = title
        print(f'Используется {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Используется {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Используется {self.title}')

drawing = Stationery('отрисовка')
drawing.draw()
print('')
pen_drawing = Pen('ручка')
pen_drawing.draw()
print('')
pencil_drawing = Pencil('карандаш')
pencil_drawing.draw()
print('')
handle_drawing = Handle('маркер')
handle_drawing.draw()