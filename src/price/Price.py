class Price:

    def __init__(self, name: str, symbol: str, price: float, last_updated: str):
        self.name = name
        self.price = price
        self.symbol = symbol
        self.last_updated = last_updated

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'symbol': self.symbol,
            'price': round(self.price, 2),
            'last_updated': self.last_updated,
        }
