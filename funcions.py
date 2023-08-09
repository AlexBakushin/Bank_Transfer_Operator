# Импорт всех необходимых библиотек для работы программы
from zipfile import ZipFile
import json
from datetime import datetime
from operator import itemgetter


class Operations:
    """
    Класс операций
    разделяет операцию на составляющие:
    """
    def __init__(self, id_, state, date, operation_amount, description, from_, to):
        """
        Инициатор класса
        :param id_: id операции
        :param state: прошла ли операция
        :param date: дата
        :param operation_amount: описание валюты
        :param description: описание
        :param from_: откуда
        :param to: куда
        """
        self.id = id_
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def date_normalised(self):
        """
        Переводит дату из операции в подходящий вид
        :return: подходящий вид
        """
        data_time = datetime.fromisoformat(self.date)
        correct_date = data_time.strftime('%d.%m.%Y')
        return correct_date

    def masquerade_account_from(self):
        """
        Маскирует номер карты или счета отправителя
        :return: замаскированный номер
        """
        if "Счет" in self.from_:
            unmasquerade_acc = self.from_
            masquerade_acc = unmasquerade_acc[:-20] + len(unmasquerade_acc[:-4]) * "*" + unmasquerade_acc[-4:]
            return masquerade_acc
        else:
            unmasquerade_acc = self.from_
            masquerade_acc = unmasquerade_acc[:-12] + ' ' + unmasquerade_acc[-12:-10] + len(
                unmasquerade_acc[-10:-8]) * "*" + ' ' + len(unmasquerade_acc[-8:-4]) * "*" + ' ' + unmasquerade_acc[-4:]
            return masquerade_acc

    def masquerade_account_to(self):
        """
        Маскирует номер карты или счета получателя
        :return: Замаскированный номер
        """
        if "Счет" in self.to:
            unmasquerade_acc = self.to
            masquerade_acc = unmasquerade_acc[:-20] + len(unmasquerade_acc[:-4]) * "*" + unmasquerade_acc[-4:]
            return masquerade_acc
        else:
            unmasquerade_acc = self.to
            masquerade_acc = unmasquerade_acc[:-12] + ' ' + unmasquerade_acc[-12:-10] + len(
                unmasquerade_acc[-10:-8]) * "*" + ' ' + len(unmasquerade_acc[-8:-4]) * "*" + ' ' + unmasquerade_acc[-4:]
            return masquerade_acc

    def operation_amount_normalised(self):
        """
        Переводит информацию о валюте в нормальный вид
        :return: информация о валюте
        """
        operation_amount_list = list(self.operation_amount.values())
        currency_list = list(operation_amount_list[1].values())
        currency = currency_list[0]
        amount = operation_amount_list[0] + ' ' + currency
        return amount

    def print(self):
        """
        Печать результата всех функций
        :return: результат
        """
        return print(f"{operation_1.date_normalised()} {self.description} \n"
                     f"{operation_1.masquerade_account_from()} -> {operation_1.masquerade_account_to()}\n"
                     f"{operation_1.operation_amount_normalised()}\n"
                     f"\n")


def opener_zip():
    """
    Берет информация из архива и переводит в массив необходимый программе,
    а также сортирует его по дате операции начиная с последних
    :return: массив с информацией об операциях
    """
    with ZipFile("operations.zip", mode="r") as operation_json:
        with operation_json.open("operations.json", mode="r") as operation_txt:
            operations_list_dict = (json.loads(operation_txt.read()))
            operations_list_list = []
            for i in operations_list_dict:
                operation_list = list(i.values())
                operations_list_list.append(operation_list)
            operations_list_list.sort()
            operations_list_list.pop(0)
            operations_list_list.sort(key=itemgetter(2), reverse=True)
            return operations_list_list


def is_executed():
    """
    Фильтрует массив
    :return: Массив с пройденными операциями
    """
    executed_list = []
    for transfer in operations_list_list:
        if transfer[1] == 'EXECUTED':
            if transfer[4] != 'Открытие вклада':
                executed_list.append(transfer)
    return executed_list[:5]


#Создание отсортированного массива из архива
operations_list_list = opener_zip()
#Фильтрация массива
executed_list = is_executed()
#Итерация массива на отдельные операции
for one_division in executed_list:
    #Деление информации об операции на составляющие
    id_, state, data, operation_amount, description, from_, to = one_division
    #Перенос составляющих в класс
    operation_1 = Operations(id_, state, data, operation_amount, description, from_, to)
    #Печать результата
    operation_1.print()
