from zipfile import ZipFile
import json
from datetime import datetime
from operator import itemgetter


class Operations:
    def __init__(self, id_, state, date, operation_amount, description, from_, to):
        self.id = id_
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def date_normalised(self):
        data_time = datetime.fromisoformat(self.date)
        correct_date = data_time.strftime('%d.%m.%Y')
        return correct_date

    def masquerade_account_from(self):
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
        operation_amount_list = list(self.operation_amount.values())
        currency_list = list(operation_amount_list[1].values())
        currency = currency_list[0]
        amount = operation_amount_list[0] + ' ' + currency
        return amount

    def print(self):
        return print(f"{operation_1.date_normalised()} {self.description} \n"
                     f"{operation_1.masquerade_account_from()} -> {operation_1.masquerade_account_to()}\n"
                     f"{operation_1.operation_amount_normalised()}\n"
                     f"\n")


def opener_zip():
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
    executed_list = []
    for transfer in operations_list_list:
        if transfer[1] == 'EXECUTED':
            if transfer[4] != 'Открытие вклада':
                executed_list.append(transfer)
    return executed_list[:5]


operations_list_list = opener_zip()
executed_list = is_executed()
for one_division in executed_list:
    id_, state, data, operation_amount, description, from_, to = one_division
    operation_1 = Operations(id_, state, data, operation_amount, description, from_, to)
    operation_1.print()
