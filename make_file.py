import argparse
from pathlib import Path

def create_file(file_path):
    """
    Создает указанный файл с помощью модуля pathlib.
    :param file_path: Путь к файлу, который нужно создать.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        file_path.touch()
        print(f"Файл {file_path} создан.")
    else:
        print(f"Файл {file_path} уже существует.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Скрипт для создания файла по указанному пути.")
    parser.add_argument("file_path", help="Путь к файлу, который нужно создать")
    args = parser.parse_args()
    if not args:
        return 1
    return create_file(args.file_path)

if __name__ == "__main__":
    main()