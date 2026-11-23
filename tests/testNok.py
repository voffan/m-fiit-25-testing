from nok import nok
import unittest

class TestNOK(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(2, nok(1,2))

    def testCase2(self):
        self.assertEqual(2, nok(2,1))

    def testCase3(self):
        self.assertEqual(1, nok(1,1))

    def testCase4(self):
        self.assertEqual(120, nok(15,8))


if __name__ == "__main__":
    unittest.main()
