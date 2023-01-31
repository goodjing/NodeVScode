import unittest


class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


class Test(unittest.TestCase):
    def setUp(self):  # 没有可以不写，或者用pass代替
        pass

    def tearDown(self):
        pass

    def testMinus(self):
        result = 5-1
        hope = 4
        self.assertEqual(result, hope)

    def testDivide(self):
        result = 5/2
        hope = 2.5
        self.assertEqual(result, hope)


if __name__ == '__main__':
    unittest.main()
