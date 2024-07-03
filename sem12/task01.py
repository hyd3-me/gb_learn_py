import csv

SUBJECTS = 'subjects.csv'
ROWS = ['Математика','Физика','История','Литература']
DESC = '''
Работа с данными студентов

Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию, выведите:

ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:

Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:

Оценка должна быть целым числом от 2 до 5

Результат теста должен быть целым числом от 0 до 100

○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.

Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
Атрибуты класса:

name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):

__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:

load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
'''

class Student():
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)
    
    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join(subject for subject in self.subjects.keys() if self.subjects.get(subject).get("grade"))}'
    
    def __setattr__(self, name, value):
        if name == 'name':
            for _name in value.split():
                if not isinstance(_name, str) or not _name.istitle():
                    raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        super().__setattr__(name, value)
        return 0
    
    def __getattr__(self, name):
        if not name in self.subjects:
            raise ValueError(f'Предмет {name} не найден')
        return 0

    def get_subjects(self):
        return 0

    def load_subjects(self, subjects_file):
        err, data = read_csv((subjects_file,))
        return {k : {'grade': [], 'test_score': []} for k in data}

    def add_grade(self, subject, grade):
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        if not self.subjects.get(subject):
            raise ValueError(f'Предмет {subject} не найден')
        self.subjects[subject]['grade'].append(grade)
    
    def add_test_score(self, subject, test_score):
        if test_score < 0 or test_score > 100:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        if not self.subjects.get(subject):
            raise ValueError(f'Предмет {subject} не найден')
        self.subjects[subject]['test_score'].append(test_score)
    
    def get_average_grade(self):
        all_grade = []
        for subject in self.subjects.keys():
            sub_grade = self.subjects.get(subject).get('grade')
            if sub_grade:
                all_grade += sub_grade
        return sum(all_grade) / len(all_grade)
    
    def get_average_test_score(self, subject):
        if not self.subjects.get(subject):
            raise ValueError(f'Предмет {subject} не найден')
        all_test_score = self.subjects.get(subject).get('test_score')
        return sum(all_test_score) / len(all_test_score)

def read_csv(args):
    with open(args[0], newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        _data = []
        for row in csvreader:
            for item in row:
                _data.append(item)
    return 0, _data

def write_csv(args):
    with open(args[0], 'w', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows([args[1]])
    return 0, 'ok'

def main():
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    print(student)

if __name__ == '__main__':
    main()