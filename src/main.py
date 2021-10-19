from requests import Session

from src.price.Notifier import Notifier
from src.price.Prices import Prices
from src.shared.Environment import Environment
from src.shared.Logger import Logger
from src.shared.Settings import Settings


# noinspection PyUnusedLocal
def handler(event, context):
    logger = Logger()

    try:
        currency = Environment.get('CURRENCY')
        price_key = Environment.get('PRICE_KEY')
        price_url = Environment.get('PRICE_URL')
        notification_url = Environment.get('NOTIFICATION_URL')

        session = Session()

        prices = Prices(session=session, currency=currency, settings=Settings(url=price_url, key=price_key))
        prices = prices.list()

        notification = Notifier(session=session, settings=Settings(url=notification_url))
        notification.send(prices)

        logger.info('Price quotes have been sent')
    except Exception as exception:
        logger.error(exception.args[0])


if __name__ == '__main__':
    handler('localhost', None)
