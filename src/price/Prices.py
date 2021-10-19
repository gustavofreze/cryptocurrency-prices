import json
from typing import List

from requests import Session

from src.price.Price import Price
from src.shared.Settings import Settings


class Prices:

    def __init__(self, session: Session, currency: str, settings: Settings):
        self.session = session
        self.currency = currency
        self.settings = settings

    def list(self, limit: int = 5) -> List[Price]:
        parameters = {
            'start': 1,
            'limit': limit,
            'convert': self.currency
        }

        self.session.headers.update({'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': self.settings.key})

        response = self.session.get(url=self.settings.url, params=parameters)
        response_data = json.loads(response.text).get('data')

        prices = []

        for data in response_data:
            quote = data.get('quote').get(self.currency)
            price = Price(
                name=data.get('name'),
                symbol=data.get('symbol'),
                price=quote.get('price'),
                last_updated=quote.get('last_updated')
            )

            prices.append(price)
        return prices
