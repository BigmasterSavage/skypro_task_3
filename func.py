import json
import datetime
from zipfile import ZipFile


def parsing_transactions(path, count: int, state: str):
    """
    Парсим файл выгрузки по операциям согласно условиям задачи
    :param path: путь до выгрузки
    :param count: количество операций для отображения
    :param state: EXECUTED или CANCELED, для задания должны быть только EXECUTED
    :return: получаем список из последних банковских операций
    """
    operations = []
    with ZipFile(path, 'r') as myzip:
        with myzip.open('operations.json', 'r') as f:
            operations_json = json.load(f)
            for i in range(len(operations_json)):
                for key, value in operations_json[i].items():
                    if key == 'state' and value == state:
                        operations.append(operations_json[i])
    return sorted(operations, key=lambda x: x['date'], reverse=True)[:count]


def output(transactions):
    """
    :param transactions: вносим результаты парсинга
    :return: получаем читаемый вывод
    """
    out = []
    for i in range(len(transactions)):
        date = datetime.datetime.strptime(transactions[i].get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        description = transactions[i].get('description')
        card_from_name = str(transactions[i].get('from')).split(" ")
        if "None" in card_from_name:
            card_from_number = "Взнос на счет"
        else:
            card_from_number = (f"{card_from_name[-1][:4]} {card_from_name[-1][4:6]}** **** "
                                f"{card_from_name[-1][-4:]}")
        card_to = (f"{''.join((str(transactions[i].get('to')).split())[:-1])} "
                   f"**{(''.join((str(transactions[i].get('to')).split())[-1]))[-4:]}")
        amount = (f"{transactions[i]['operationAmount'].get('amount')} "
                  f"{transactions[i]['operationAmount']['currency'].get('name')}")

        print_info = f"""
{date.strftime('%d.%m.%Y')} {description}
{" ".join(card_from_name[:-1])} {card_from_number} -> {card_to}
{amount}
"""
        out.append(print_info)
    return out

