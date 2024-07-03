
DESC = '''
Управление информацией о сотрудниках и их возрасте

В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.'''

class InvalidNameError(ValueError):
    pass
class InvalidAgeError(ValueError):
    pass
class InvalidIdError(ValueError):
    pass

class Person:
    def __init__(self, name, firstname, lastname, age):
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __setattr__(self, name, value):
        if name in ('name', 'firstname', 'lastname'):
            if not value:
                raise InvalidNameError('Invalid name: . Name should be a non-empty string.')
        if name == 'age':
            if value < 0 or not isinstance(value, int):
                raise InvalidAgeError('Invalid age: -5. Age should be a positive integer.')
        super().__setattr__(name, value)

    def __str__(self):
        return f'{self.name} {self.firstname} {self.lastname} - {self.age}'

    def birthday(self):
        self.age += 1
    
    def get_age(self):
        return self.age

class Employee(Person):
    _id = 1

    @classmethod
    def get_id(cls):
        _old_id = cls._id
        cls._id += 1
        return _old_id
    
    def __new__(cls, *args):
        return super().__new__(cls)
    
    def __init__(self, name, firstname, lastname, age, _id):
        self._id = _id
        super().__init__(name, firstname, lastname, age)
    
    def __setattr__(self, name, value):
        if name == '_id':
            if value < 100000 or value > 999999:
                raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')
        return super().__setattr__(name, value)
    
    def get_level(self):
        return sum(int (val)for val in str(self.age)) % 7


def main():
    # pers = Person('pers1', 'pers2', 'pers3', 23)
    emp1 = Employee('name1', 'name2', 'name3', 33, 123456)
    emp2 = Employee('name1', 'name2', 'name3', 34, 654321)
    print(emp1._id, emp1.get_level())
    print(emp2._id, emp2.get_level())

if __name__ == '__main__':
    main()
