import unittest
from nok import nod


class TestNOKWB(unittest.TestCase):

    def testCase1(self):
        result = nod(36,15)
        self.assertEqual(3, result)

    def testCase2(self):
        with self.assertRaises(Exception):
            nod(-5,15)

    def testCase3(self):
        with self.assertRaises(Exception):
            nod(5,-5)

    def testCase4(self):
        with self.assertRaises(Exception):
            nod(5.5, 15)

    def testCase5(self):
        with self.assertRaises(Exception):
            nod(5, 15.6)

    def testCase6(self):
        self.assertAlmostEqual(0.3333, 1/3, delta=4)


if __name__ == "__main__":
    unittest.main()
