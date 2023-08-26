import unittest
from main import *
from func import *


state: str = "EXECUTED"
count: int = 5
path = PATH


class FuncTest(unittest.TestCase):
    """
    Тестим функции парсинга и формы для вывода
    """

    def setUp(self):
        self.parsing = parsing_transactions(path=path, count=count, state=state)
        self.parsing_count = len(self.parsing)

    def test_count(self):
        """
        Проверяем количество спарсеных операций
        """
        count = 0
        for i in range(self.parsing_count):
            if bool(i + 1):
                count += 1
        self.assertNotEquals(count, 0)
        self.assertEquals(count, 5)

    def test_state_input_correct(self):
        """
        Првоеряем корректность фильтра парсинга
        """
        for i in range(self.parsing_count):
            for key, value in self.parsing[i].items():
                if key == "state":
                    self.assertEquals(value, state)

    def test_correct_parsing_keys(self):
        """
        Проверяем корретность спарсеных ключей
        """
        for i in range(self.parsing_count):
            parsing_keys = list(self.parsing[i])
            self.assertEquals(parsing_keys[0], "id")
            self.assertEquals(parsing_keys[1], "state")
            self.assertEquals(parsing_keys[2], "date")
            self.assertEquals(parsing_keys[3], "operationAmount")
            self.assertEquals(list(self.parsing[i][parsing_keys[3]])[0], "amount")
            self.assertEquals(list(self.parsing[i][parsing_keys[3]])[1], "currency")
            self.assertEquals(list(self.parsing[i][list(self.parsing[i])[3]][list(self.parsing[i][list(self.parsing[i])[3]])[1]])[0], "name")
            self.assertEquals(list(self.parsing[i][list(self.parsing[i])[3]][list(self.parsing[i][list(self.parsing[i])[3]])[1]])[1], "code")
            self.assertEquals(parsing_keys[4], "description")

    def test_output(self):
        """
        Проверяем что пользователю вышел НЕ пустой экран
        """
        for i in output(self.parsing):
            self.assertIsNotNone(i)
            self.assertIn("->", i)
