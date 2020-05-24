import unittest

class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        """
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.assertTrue(True)

    def testFailUnless(self):
        """
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.assertTrue(True)

    def testFailIf(self):
        """
        :return:
        """
        self.assertFalse(False)

    def testAssertFalse(self):
        """
        Если значение аргумент != False, то кидает ошибку
        :return:
        """
        self.assertFalse(False)

    def testEqual(self):
        """
        Проверка равенства двух аргументов
        :return:
        """
        self.assertEqual(1, 3 - 2)

    def testNotEqual(self):
        """
        Проверка НЕ равенства двух аргументов
        :return:
        """
        self.assertNotEqual(2, 3 - 2)

    def testEqualFail(self):
        """
        Ругается если значение аргументов равно
        :return:
        """
        self.assertNotEqual(1, 2)

    def testNotEqualFail(self):
        """
        Ругается если значение аргументов не равно
        :return:
        """
        self.assertEqual(2, 3 - 1)

    def testNotAlmostEqual(self):
        """
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения равны
        :return:
        """
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        """
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения не равны
        :return:
        """
        self.assertAlmostEqual(1.1, 3.3 - 2.0, places=0)


if __name__ == '__main__':
    unittest.main()