import pathlib
import json
import csv
import pickle


DESC ='''
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория. Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:

Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий. При этом сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), и затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)), и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого. Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
'''

_RES = {}
result = []

def process_file(_fpath):
    f_name = str(_fpath)
    f_size = _fpath.stat().st_size
    file_info = {
            'Path': f_name,
            'Type': 'File',
            'Size': f_size,
        }
    _RES[f_name] = file_info
    return f_size

def process_dir(_dpath):
    _dname = str(_dpath)
    _RES[_dname] = {}
    _dir_size = dir_crawler(_dpath)
    _dir_info = {
        'Path': _dname,
        'Type': 'Directory',
        'Size': _dir_size,
    }
    _RES[_dname] = _dir_info
    return _dir_size

def dir_crawler(directory, _parent=None):
    directory = pathlib.Path(directory)
    dir_size = 0
    _dirs = []
    if _parent:
        process_dir(directory)
    for _path in directory.glob('*'):
        if _path.is_file():
            dir_size += process_file(_path)
        if _path.is_dir():
            _dirs.append(_path)
    for _dir in _dirs:
        dir_size += dir_crawler(_dir, _parent=True)
    return dir_size

def get_result_list():
    for k, v in _RES.items():
        result.append(v)
    return result

def save_results_to_json(_res, _fpath):
    with open(_fpath, 'w') as _file:
        json.dump(_res, _file)
    return 0

def save_results_to_csv(_res, _fpath):
    fieldnames = ['Path', 'Type', 'Size']
    with open(_fpath, 'w', newline='\n') as _file:
        writer = csv.DictWriter(_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(_res)
    return 0

def save_results_to_pickle(_res, _fpath):
    with open(_fpath, 'wb') as _file:
        pickle.dump(_res, _file)
    return 0

def traverse_directory(_path):
    dir_crawler(_path)
    return get_result_list()

def main():
    direcotory = 'geekbrains'
    traverse_directory(direcotory)
    err = save_results_to_json(result, 'sem08/result.json')
    err = save_results_to_csv(result, 'sem08/result.csv')
    err = save_results_to_pickle(result, 'sem08/result.pickle')
    if err:
        print('error')
    else:
        print('ok')

def test_func():
    print(f'hello from task01')

if __name__ == '__main__':
    main()
