import pathlib


DESC = '''Пакет для работы с файлами 3

Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
'''

_TXT = '''
def generate_csv_file(file_name, rows):
    _csv_rows = []
    for _ in range(rows):
        nums = [random.randint(1, 63) for _ in range(3)]
        _csv_rows.append([f'{nums[0]}', f'{nums[1]}', f'{nums[2]}'])
    err = write_csv(file_name, _csv_rows)

def save_to_json(func):
    def do_func(*args):
        _final_list = []
        with open(args[0], 'r') as _infile:
            reader = csv.reader(_infile, delimiter='\t')
            for row in reader:
                _final_list.append({'parameters': row, 'result': 'ok'})
        with open('results.json', 'w') as _file:
            json.dump(_final_list, _file)
    return do_func

@save_to_json
def find_roots(a, b, c):
    pass
'''

def main():
    f_name = '__init__.py'
    f_path = pathlib.Path().cwd() / f_name
    f_path.write_text(_TXT)


if __name__ == '__main__':
    main()