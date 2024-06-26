import pathlib
import json
import random
import csv


DESC = '''Генерация случайных данных и нахождение корней квадратного уравнения

Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

    Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:

Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

На входе:

generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:

True
True

Формат JSON файла определён следующим образом:

[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]
'''

def write_csv(_fname, _data):
    with open(_fname, 'w') as _file:
        file_writer = csv.writer(_file, delimiter = "\t")
        file_writer.writerows(_data)
    # print(f'{_fname} has been writed')
    return 0

def generate_csv_file(file_name, rows):
    _csv_rows = []
    for _ in range(rows):
        _csv_rows.append([random.randint(1, 63) for _ in range(3)])
    err = write_csv(file_name, _csv_rows)

def save_to_json(func):
    def do_func(*args):
        _final_list = []
        with open(args[0], 'r') as _infile:
            reader = csv.reader(_infile, delimiter='\t')
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                _final_list.append({'parameters': [a, b, c], 'result': result})
        with open('results.json', 'w') as _file:
            json.dump(_final_list, _file)
    return do_func

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")
    with open("results.json", 'r') as f:
        data = json.load(f)
    if 100<=len(data)<=1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
    print(len(data)==101)
