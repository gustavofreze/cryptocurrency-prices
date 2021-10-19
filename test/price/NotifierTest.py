import datetime
from random import uniform
from unittest import TestCase
from unittest.mock import MagicMock

from src.price.Notifier import Notifier
from src.price.Price import Price
from src.shared.Environment import Environment
from src.shared.Settings import Settings


class NotifierTest(TestCase):
    url = Environment.get('NOTIFICATION_URL')

    def test_when_notification_is_sent(self):
        session = MagicMock()
        session.return_value.status_code.return_value = 200
        last_updated = datetime.datetime.now().astimezone().isoformat()
        notification = Notifier(session=session, settings=Settings(url=self.url))

        """Given a price list"""
        prices = [
            Price(name="Bitcoin", symbol="BTC", price=uniform(50_000.00, 1_000_000.00), last_updated=last_updated),
            Price(name="Ethereum", symbol="ETH", price=uniform(20_000.00, 100_000.00), last_updated=last_updated)
        ]

        """When the notification was sent"""
        notification.send(prices)

        """Then the post method is called"""
        session.post.assert_called()
