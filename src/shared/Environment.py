import os


class Environment:

    @staticmethod
    def get(variable: str) -> str:
        environment = os.getenv(variable)

        if environment is None:
            raise Exception('Environment variable %s is missing' % variable)
        return environment
