import unittest
import time


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start!')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('end!')

    def test01(self):
        print('执行测试用例01')

    def test03(self):
        print('执行测试用例02')

    def test02(self):
        print('执行测试用例02')

    def addtest(self):
        print('add方法')


if __name__ == "__main__":
    unittest.main()
