import unittest
import script


class TestMain(unittest.TestCase):
    def test1(self):
        test_param = 5
        result = script.add_five(test_param)
        self.assertEqual(result, 10)

    def test2(self):
        test_param = 0
        result = script.add_five(test_param)
        self.assertEqual(result, 'number should be greater than zero')

    def test3(self):
        test_param = -1
        result = script.add_five(test_param)
        self.assertEqual(result, 'number should be greater than zero')


unittest.main()
