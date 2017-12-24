import unittest
from Jzon import isClass, jsonify, unJsonify, parse_from_dict
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
        self.assertEqual(isClass(model()), True)
        self.assertEqual(isClass(None), False)

    def test_array_Serialization(self):
        # Array of Strings
        a = ["gvdrfg", "fsef", "fsef", "fserfgser"]
        f = unJsonify(jsonify(a))
        self.assertEqual(len(a), len(f))
        i = 0
        while(i < len(a)):
            self.assertEqual(a[i] in f, True)
            i += 1

        # Array of numbers
        a = [1, 2, 3, 4]
        f = unJsonify(jsonify(a))
        self.assertEqual(len(a), len(f))
        i = 0
        while(i < len(a)):
            self.assertEqual(a[i] in f, True)
            i += 1

        # Array of floats
        a = [1.456, 2.343, 0.3, 1.4]
        f = unJsonify(jsonify(a))
        self.assertEqual(len(a), len(f))
        i = 0
        while(i < len(a)):
            self.assertEqual(a[i] in f, True)
            i += 1

        # Array of dicts
        a = [{"fe": "vr"}, {"f": 52}, {"ff": 3.4}, {"de": 52, "rr": "rgr"}]
        f = unJsonify(jsonify(a))
        self.assertEqual(len(a), len(f))
        i = 0
        while(i < len(a)):
            self.assertEqual(a[i] in f, True)
            i += 1

    def test_classObject_Serialization(self):

        # Complex object Serialization Strongly Typed
        a = model()
        a.id = 0
        a.name = "Miguel Ángel Campos"
        a.salary = 100.45
        a.none = None

        a.model1 = model2()
        a.model1.salary = 100.45
        a.model1.new_employee = True

        a.bo = "None"
        a.fff = None
        a.date = datetime.datetime(2001, 1, 1)
        a.c = 1 + 2j
        a.g = []
        a.g.append(a.model1)

        modelr = unJsonify(jsonify(a), model())

        self.assertTrue(isinstance(modelr, model))
        self.assertTrue(isinstance(modelr.model1, model2))
        self.assertEqual(modelr.name, a.name)
        self.assertEqual(modelr.id, a.id)
        self.assertEqual(modelr.salary, a.salary)
        self.assertEqual(modelr.bo, a.bo)
        self.assertEqual(modelr.fff, a.fff)
        #self.assertEqual(modelr.date, a.date)

        # Give Type to list element by using parse_from_dict
        modelr.g.append(parse_from_dict(model2(),modelr.g.pop()))
        
        self.assertEqual(modelr.g[0].salary, a.g[0].salary)
        self.assertEqual(modelr.g[0].new_employee, a.g[0].new_employee)

        self.assertEqual(modelr.model1.salary, a.model1.salary)
        self.assertEqual(modelr.model1.new_employee, a.model1.new_employee)


if __name__ == '__main__':
    unittest.main()


class model(object):
    def __init__(self):
        self.id = 0
        self.name = "Miguel Ángel Campos"
        self.salary = 100.45
        self.none = None
        self.model1 = model2()
        self.bo = "None"
        self.fff = None
        self.date = datetime.datetime.today()
        self.c = 1 + 2j
        self.g = []
        self.g.append(model2())


class model2(object):
    def __init__(self):
        self.salary = 100.45
        self.new_employee = True
