import unittest

from mock import call, Mock

from ..event import Event

class EventTest(unittest.TestCase):

    def test_add_listeners(self):
        event = Event()
        l1 = Mock()
        l2 = Mock()
        event += l1
        event += l2

        event(1, 2, 3)

        self.assertEqual(l1.call_args, call(1, 2, 3))
        self.assertEqual(l2.call_args, call(1, 2, 3))

