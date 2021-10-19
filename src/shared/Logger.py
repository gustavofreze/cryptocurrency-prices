import logging
import sys


class Logger:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

    def info(self, message: str):
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def error(self, message: str):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)
