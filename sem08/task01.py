import pathlib


def get_size_recursive(_path):
    total_size = 0

    if _path.is_file():
        return _path.stat().st_size
    for item in _path.iterdir():
        if item.is_dir():
            total_size += get_size_recursive(item)
        elif item.is_file():
            total_size += item.stat().st_size
    return total_size

def main():
    current_direcotory = pathlib.Path('.')
    total_size = get_size_recursive(current_direcotory)
    print(f'total size: {total_size}')

if __name__ == '__main__':
    main()