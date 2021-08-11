import sys
sys.path.append('../../python-design-patterns')


from unittest import TestCase
from behavioral.command import Command, Receiver, Invoker

class ReceiverTestCase(TestCase):

    def setUp(self):

        class Thermostat(Receiver):

            def raise_temp(self, amount):
                return "Temperature raised by {0} degrees".format(amount)

            def lower_temp(self, amount):
                return "Temperature lowered by {0} degrees".format(amount)

        self.thermostat = Thermostat()

    def test_valid_action(self):

        self.assertEqual("Temperature raised by 5 degrees", self.thermostat.action('raise_temp', 5))
        self.assertEqual('Temperature lowered by 5 degrees', self.thermostat.action('lower_temp', 5))

