from unittest import TestCase

from mock import call, Mock, patch

from ..main import main

MODULE_UNDER_TEST = 'zerkcom.main.'

class MainTest(TestCase):

    @patch(MODULE_UNDER_TEST + 'sys.argv', ['zerkcom', 'arg'])
    @patch(MODULE_UNDER_TEST + 'create_parser')
    @patch(MODULE_UNDER_TEST + 'pyglet', Mock())
    def test_main(
        self, mock_create_parser
    ):

        main()

        self.assertEqual(mock_create_parser.call_args, call())
        self.assertEqual(
            mock_create_parser.return_value.parse_args.call_args,
            call(['arg'])
        )

