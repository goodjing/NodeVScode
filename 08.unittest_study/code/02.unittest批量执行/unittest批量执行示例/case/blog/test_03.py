import time
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print('start!')

    def tearDown(self):
        time.sleep(2)
        print('end!')

    def test03(self):
        print('执行测试用例test03')


if __name__ == '__main__':
    unittest.main()