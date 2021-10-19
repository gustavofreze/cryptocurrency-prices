from unittest import TestCase

from src.shared.Environment import Environment


class EnvironmentTest(TestCase):

    def test_environment_get_variable(self):
        environment = Environment()

        """Given a variable that is defined"""
        variable = 'CURRENCY'

        """When the get method is called"""
        value = environment.get(variable)

        """Then return a value"""
        self.assertIsNotNone(value)

    def test_environment_variable_is_missing(self):
        environment = Environment()

        with self.assertRaises(Exception) as context:
            """Given a variable that is not defined"""
            variable = 'XPTO'

            """When the get method is called"""
            environment.get(variable)

        """Then return an error"""
        self.assertEqual('Environment variable XPTO is missing', context.exception.args[0])
