import unittest

from name_function import get_formatted


class NamesTestCase(unittest.TestCase):
    '''测试name_function'''

    def test_first_last(self):
        formatted = get_formatted('f', 'l')
        print(formatted)
        self.assertEqual(formatted, 'f l')


unittest.main()
