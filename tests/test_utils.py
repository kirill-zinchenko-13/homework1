import unittest
from unittest.mock import patch, Mock
from src.external_api import get_exchange_rate, convert_to_rub

class TestCurrencyFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_get_exchange_rate_success(self, mock_get):
        # Настройка мока для успешного ответа от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'RUB': 75.0
            }
        }
        mock_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertEqual(result, 75.0)

    @patch('requests.get')
    def test_get_exchange_rate_failure(self, mock_get):
        # Настройка мока для ошибки при запросе
        mock_get.side_effect = requests.exceptions.HTTPError("Ошибка HTTP")

        result = get_exchange_rate('USD')
        self.assertIsNone(result)

    @patch('requests.get')
    def test_get_exchange_rate_no_rub(self, mock_get):
        # Настройка мока для ответа без RUB в rates
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'EUR': 90.0
            }
        }
        mock_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertIsNone(result)

    def test_convert_to_rub_with_rub(self):
        transaction = {'amount': 1000, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 1000.0)

    @patch('your_module.get_exchange_rate')  # Патчинг функции get_exchange_rate
    def test_convert_to_rub_with_other_currency(self, mock_get_exchange_rate):
        transaction = {'amount': 100, 'currency': 'USD'}
        mock_get_exchange_rate.return_value = 75.0  # Настройка мока для курса USD к RUB

        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)  # 100 * 75.0

    @patch('your_module.get_exchange_rate')  # Патчинг функции get_exchange_rate
    def test_convert_to_rub_currency_not_found(self, mock_get_exchange_rate):
        transaction = {'amount': 100, 'currency': 'USD'}
        mock_get_exchange_rate.return_value = None  # Курс не найден

        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)  # Ожидаем 0.0 из-за отсутствия курса

if __name__ == '__main__':
    unittest.main()