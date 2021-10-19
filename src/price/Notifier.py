from typing import List

from requests import Session

from src.price.Price import Price
from src.shared.Settings import Settings


class Notifier:

    def __init__(self, session: Session, settings: Settings):
        self.session = session
        self.settings = settings

    def send(self, prices: List[Price]):
        self.session.headers.update({'Content-Type': 'application/json'})
        self.session.post(url=self.settings.url, json=[price.to_dict() for price in prices])
