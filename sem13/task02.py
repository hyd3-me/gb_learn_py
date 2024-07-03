from typing import Any, Union

DESC = '''
Обработка исключений в Archive

Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является пустой строкой.

Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'

И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с плавающей запятой.

Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'''


class InvalidTextError(ValueError):
    pass

class InvalidNumberError(ValueError):
    pass


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number
    
    def __setattr__(self, name, value):
        if not name in ('text', 'number', 'archive_text', 'archive_number'):
            raise AttributeError(f'invalid attribute')
        if name == 'text':
            if not isinstance(value, str) or not value:
                raise InvalidTextError(f'Invalid text: {value}. Text should be a non-empty string.')
        if name == 'number':
            if not isinstance(value, int) and not isinstance(value, float) or value < 0:
                raise InvalidNumberError(f'Invalid number: {value}. Number should be a positive integer or float.')
        super().__setattr__(name, value)

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'



def main():
    archive_instance = Archive("Sample text", 42.5)
    print(archive_instance)


if __name__ == '__main__':
    main()
