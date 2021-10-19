import datetime
import json
from unittest import TestCase
from unittest.mock import MagicMock

from src.price.Prices import Prices
from src.shared.Environment import Environment
from src.shared.Settings import Settings


class PricesTest(TestCase):
    url = Environment.get('PRICE_URL')
    key = Environment.get('PRICE_KEY')
    currency = Environment.get('CURRENCY')

    def test_when_list_is_used_with_limit(self):
        payload = {
            'data': [
                {
                    'id': 1,
                    'name': 'Bitcoin',
                    'symbol': 'BTC',
                    'quote': {
                        'USD': {
                            'price': 57434.24099023865,
                            'last_updated': datetime.datetime.now().astimezone().isoformat()
                        }
                    }
                }
            ]
        }

        session = MagicMock()
        session.get.return_value.text = json.dumps(payload)
        prices = Prices(session=session, currency=self.currency, settings=Settings(url=self.url, key=self.key))

        """Given I have a price quote, When limit for list is set"""
        limit = 1

        """And the list called"""
        prices = prices.list(limit)

        """Then the amount of results must equal the limit"""
        self.assertEqual(1, len(prices))
        session.get.assert_called()
