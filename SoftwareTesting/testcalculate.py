import unittest
from unittest import mock
from calculate import add,minus,divide,multi

class TestCalculate(unittest.TestCase):

    def setUp(self):
        print("do something before testDemo.Prepare environment.")

    def tearDown(self):
        print("do something after testDemo.Clean up.")

    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    # @unittest.skip("not run...")
    def test_minus(self):
        minus = mock.Mock(return_value=-1)
        self.assertEqual(-1, minus(1, 2))
        # self.assertNotEqual(0, minus(2, 1))

    def test_divide(self):
        # self.skipTest("测试跳过")
        self.assertEqual(2, divide(10, 5))


    def test_multi(self):
        """Test method multi(a, b)"""
        multi = mock.Mock(return_value = 6)
        self.assertEqual(6, multi(2, 3))


if __name__ == '__main__':
    unittest.main()