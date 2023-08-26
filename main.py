import os
from func import parsing_transactions, output


def main():

    PATH = os.path.join(os.path.dirname(__file__), 'info', 'operations.zip')
    number_of_operations = 5
    state_operations = "EXECUTED"

    parsing = parsing_transactions(path=PATH, count=number_of_operations, state=state_operations)
    for i in output(parsing):
        print(i)


if __name__ == '__main__':
    main()

