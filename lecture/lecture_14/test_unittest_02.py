import io  # модуль input output ввод, вывод информации
import unittest
from unittest.mock import patch  # расширение функционала

from prime_unittest import is_prime


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(42))  # вернуть ложь при проверке на простое число 42, т.е. asser ждет False
        self.assertTrue(is_prime(73))

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)
        # assert (вызов) ждет исключение (Raises) TypeError при 3.14,
        # при этом передается три параметра (ошибка, функция, значение)

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)

    @patch('sys.stdout', new_callable=io.StringIO)  # в декоратор передаем стандартный поток вывода ('sys.stdout')
    # new_callable=io.StringIO хотим перехватить стандартный поток ввода вывода
    def test_warning_false(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))  # то есть mock_stdout перехватиться
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long time. Working...\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long time. Working...\n')


if __name__ == '__main__':
    unittest.main()
