import pathlib


DESC = '''
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
'''

_TXT = '''
def get_dir_size(_path):
    return 0

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
'''

def main():
    f_name = '__init__.py'
    f_path = pathlib.Path().cwd() / f_name
    f_path.write_text(_TXT)


if __name__ == '__main__':
    main()