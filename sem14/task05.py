import pytest

class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже
def test_width():
    r1 = Rectangle(5)
    assert r1.width == 5, 'width not 5'

def test_height():
    r1 = Rectangle(3, 4)
    assert r1.height == 4, 'height not 4'

def test_perimeter():
    r1 = Rectangle(5)
    assert r1.perimeter() == 20, 'perimeter not 20'

def test_area():
    r1 = Rectangle(3, 4)
    assert r1.area() == 12, 'area is not 12'

def test_addition():
    r1 = Rectangle(5, 3)
    r2 = Rectangle(1, 4)
    r3 = r1 + r2
    assert r3.width == 3 and r3.height == 7, 'wrong addition'

def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)

def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)

def test_set_width():
    r1 = Rectangle(5)
    r1.width = 10
    assert r1.width == 10, 'width not 10'

def test_set_negative_width():
    r1 = Rectangle(5)
    with pytest.raises(NegativeValueError):
        r1.width = -10

def test_set_height():
    r1 = Rectangle(3, 4)
    r1.height = 6
    assert r1.height == 6, 'dont set height to 6'

def test_set_negative_height():
    r1 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError):
        r1.height = -6

def test_subtraction():
    r1 = Rectangle(10, 1)
    r2 = Rectangle(3, 4)
    r3 = r1 - r2
    assert r3.width == 9 and r3.height == 9, 'wrong subtraction'

def test_subtraction_negative_result():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(10, 1)
    with pytest.raises(NegativeValueError):
        r3 = r1 - r2

def test_subtraction_same_perimeter():
    r1 = Rectangle(5, 1)
    r2 = Rectangle(4, 3)
    with pytest.raises(NegativeValueError):
        r3 = r1 - r2