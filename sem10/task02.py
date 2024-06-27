DESC = '''
Лотерея Класс

На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Пример выходных данных:

Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
'''


class LotteryGame:
    def __init__(self, list1, list2):
        self._list1 = list1
        self._list2 = list2

    def compare_lists1(self):
        """
        Сравнивает два списка чисел и выводит количество совпадающих чисел.

        :_list1: Список чисел из вашего билета.
        :_list2: Список чисел, которые выпали в лотерее.
        """
        f_nums = set(self._list1) & set(self._list2)
        common_numbers = len(f_nums)
        if common_numbers == 0:
            print("Совпадающих чисел нет.")
        else:
            print(f'Совпадающие числа: {list(f_nums)}\nКоличество совпадающих чисел: {common_numbers}')
    
    def compare_lists(self):
        f_list = []
        for num in self._list1:
            if num in self._list2:
                f_list.append(num)
        if len(f_list) == 0:
            print("Совпадающих чисел нет.")
        else:
            print(f'Совпадающие числа: {f_list}\nКоличество совпадающих чисел: {len(f_list)}')

# Использование класса

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]


game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()