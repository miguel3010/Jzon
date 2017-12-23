import unittest
from Jzon import isClass
import datetime


class TestProblem(unittest.TestCase):

    def test_isClass(self):

        self.assertEqual(isClass(True), False)
        self.assertEqual(isClass(False), False)
        self.assertEqual(isClass(2), False)
        self.assertEqual(isClass(2.8), False)
        self.assertEqual(isClass(datetime.datetime.today()), False)
        self.assertEqual(isClass(1 + 2j), False)
        self.assertEqual(isClass([2, 3, 4]), False)
        f = ["vsd", "vsd"]
        self.assertEqual(isClass(f), False)
         
        self.assertEqual(isinstance(ii(), object), True)
        self.assertEqual(isClass(ii()), True)


if __name__ == '__main__':
    unittest.main()

class ii(object):
    pass