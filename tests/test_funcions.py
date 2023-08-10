from Kursovaya_5.funcions import Operations, is_executed


def test_date_normalised():
    operation_1 = Operations(782295999, 'EXECUTED', '2019-09-11T17:30:34.445824',
                             {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}}, 'Перевод организации',
                             'Счет 24763316288121894080', 'Счет 96291777776753236930')
    assert operation_1.date_normalised() == '11.09.2019'
    operation_2 = Operations(86608620, 'CANCELED', '2019-08-16T04:23:41.621065',
                             {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'Перевод с карты на счет',
                             'MasterCard 8826230888662405', 'Счет 96119739109420349721')
    assert operation_2.date_normalised() == '16.08.2019'


def test_masquerade_account_from():
    operation_2 = Operations(86608620, 'CANCELED', '2019-08-16T04:23:41.621065',
                             {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'Перевод с карты на счет',
                             'MasterCard 8826230888662405', 'Счет 96119739109420349721')
    assert operation_2.masquerade_account_from() == 'MasterCard 8826 23** **** 2405'


def test_masquerade_account_to():
    operation_2 = Operations(86608620, 'CANCELED', '2019-08-16T04:23:41.621065',
                             {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'Перевод с карты на карту',
                             'MasterCard 8826230888662405', 'Visa Gold 7756673469642839')
    assert operation_2.masquerade_account_to() == 'Visa Gold 7756 67** **** 2839'


def test_operation_amount_normalised():
    operation_1 = Operations(782295999, 'EXECUTED', '2019-09-11T17:30:34.445824',
                             {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}}, 'Перевод организации',
                             'Счет 24763316288121894080', 'Счет 96291777776753236930')
    assert operation_1.operation_amount_normalised() == '54280.01 USD'
    operation_2 = Operations(86608620, 'CANCELED', '2019-08-16T04:23:41.621065',
                             {'amount': '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'Перевод с карты на счет',
                             'MasterCard 8826230888662405', 'Счет 96119739109420349721')
    assert operation_2.operation_amount_normalised() == '6004.00 руб.'


def test_print():
    operation_2 = Operations(114832369, 'EXECUTED', '2019-12-07T06:17:14.634890',
                             {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'Перевод организации',
                             'Visa Classic 2842878893689012', 'Счет 35158586384610753655')
    assert operation_2.print() == print(f"07.12.2019 Перевод организации \n"
                                        f"Visa Classic 2842 87** **** 9012 -> Счет ****************3655\n"
                                        f"48150.39 USD\n"
                                        f"\n")


def test_is_executed():
    operation_list = is_executed()
    assert operation_list == [[114832369, 'EXECUTED', '2019-12-07T06:17:14.634890',
                               {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'Перевод организации', 'Visa Classic 2842878893689012', 'Счет 35158586384610753655'],
                              [154927927, 'EXECUTED', '2019-11-19T09:22:25.899614',
                               {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'Перевод организации', 'Maestro 7810846596785568', 'Счет 43241152692663622869'],
                              [482520625, 'EXECUTED', '2019-11-13T17:38:04.800051',
                               {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'Перевод со счета на счет', 'Счет 38611439522855669794', 'Счет 46765464282437878125'],
                              [509645757, 'EXECUTED', '2019-10-30T01:49:52.939296',
                               {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'Перевод с карты на счет', 'Visa Gold 7756673469642839', 'Счет 48943806953649539453'],
                              [888407131, 'EXECUTED', '2019-09-29T14:25:28.588059',
                               {'amount': '45849.53', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'Перевод со счета на счет', 'Счет 35421428450077339637', 'Счет 46723050671868944961']]
