from func import parsing_transactions, output
from system_info import PATH


def main():
    """
    Запускаем все что написали под капотом в func.py с нужными пользователю параметрами
    :return: получаем выводы по операциям согласно запросу пользователя
    """
    number_of_operations = 5
    state_operations = "EXECUTED"
    parsing = parsing_transactions(path=PATH, count=number_of_operations, state=state_operations)
    for i in output(parsing):
        print(i)


if __name__ == '__main__':
    main()

