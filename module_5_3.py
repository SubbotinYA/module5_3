# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
# Необходимо дополнить класс House следующими специальными методами:

# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты
# сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:

class House:
    def __init__(self, name:str, number_of_floors:int):
        """Иницилизируем экзепляр по аттрибутам"""
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        """ Охарактеризум объект по озрасту"""
        return self.number_of_floors

    def __str__(self):
        """не строгое описание экземпляра"""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor:int):
        if 1 <= new_floor <= self.number_of_floors:
            go_to = [x for x in range(1, new_floor + 1)]
            print(*go_to)
        else:
            print(f"{new_floor} этажа не существует в доме {self.name!r}")

    def __eq__(self, other):
        """Методом сравнения на равенства: возвращаем True, если количество этажей self == other """
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')

        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        """Методом сравнения "меньше чем" (Lower than)"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        """Методом сравнения "меньше или равно"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """Методом сравнения "больше чем" (Greater than)"""

        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """Методом сравнения "больше или равно"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """Методом сравнения на неравенство"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        """Методом добавления элемента в множество"""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения только из целых чисел')
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        """Методом симметричного сложения"""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения из целых чисел ')
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        """Методом сложения с присваиванием +="""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения из целых чисел ')
        self.number_of_floors += value
        return self

    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__

print('h1+10=',h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

