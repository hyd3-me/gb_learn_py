

DESC = '''
Класс Rectangle - работа с прямоугольниками doctest

Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи. Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError с текстом Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4. При необходимости выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:

__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})
'''

class NegativeValueError(ValueError):
    pass

# Введите ваше решение ниже
class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width < 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}.')
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"

def est_width(num):
    """
    test_width(5)
    True
    test_width(-2)
    Traceback (most recent call last):
     ...
    NegativeValueError: Ширина должна быть положительной, а не -2.
    """
    if num == 5:
        r1 = Rectangle(5)
        return r1.width == 5
    else:
        r4 = Rectangle(-2)

def test_addition():
    """
    >>> test_addition()
    6.0
    """

    r1 = Rectangle(5)
    r2 = Rectangle(3, 4)
    r3 = r1 + r2
    return r3.height