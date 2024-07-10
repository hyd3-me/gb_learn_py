import doctest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 'j', 100)
        >>> emp1.full_name()
        'Ivanov Ivan Ivanovich'
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 'manager', 50000)
        >>> emp1.raise_salary(10)
        >>> emp1.salary
        55000.0
        """
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


# Введите ваше решение ниже