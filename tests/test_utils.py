import os
import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_to_rub, get_exchange_rate


class TestCurrencyConverter(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_get_exchange_rate_success(self, mock_get):
        # Настройка mock-ответа
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'RUB': 75.0}}
        mock_response.raise_for_status = Mock()  # Не вызывает ошибку
        mock_get.return_value = mock_response

        result = get_exchange_rate('USD')
        self.assertEqual(result, 75.0)
        mock_get.assert_called_once_with(
            'https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB',
            headers={"apikey": os.getenv("API_KEY")}
        )

    @patch('external_api.requests.get')
    def test_get_exchange_rate_no_rub_in_rates(self, mock_get):
        # Настройка mock-ответа без RUB в rates
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {}}
        mock_response.raise_for_status = Mock()  # Не вызывает ошибку
        mock_get.return_value = mock_response

        result = get_exchange_rate('EUR')
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch('external_api.requests.get')
    def test_get_exchange_rate_exception(self, mock_get):
        # Настройка mock-ответа для выбрасывания исключения
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка сети")

        result = get_exchange_rate('GBP')
        self.assertIsNone(result)
        mock_get.assert_called_once()

    def test_convert_to_rub_already_in_rub(self):
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_success(self, mock_get_exchange_rate):
        # Настройка mock-ответа для get_exchange_rate
        mock_get_exchange_rate.return_value = 75.0

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)
        mock_get_exchange_rate.assert_called_once_with('USD')

    @patch('external_api.get_exchange_rate')
    def test_convert_to_rub_no_exchange_rate(self, mock_get_exchange_rate):
        # Настройка mock-ответа для get_exchange_rate, который возвращает None
        mock_get_exchange_rate.return_value = None

        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)
        mock_get_exchange_rate.assert_called_once_with('EUR')


if __name__ == '__main__':
    unittest.main()
