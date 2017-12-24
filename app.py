import datetime
import json

from Jzon import jsonify, unJsonify


class model(object):
    def __init__(self):
        self.id = 0
        self.name = "Miguel Ángel Campos"
        self.salary = 100.45
        self.model1 = model2()
        self.bo = "None"
        gg = {}
        gg['a'] = 'alpha'
        gg['g'] = 'gamma'
        gg['o'] = 'omega'
        self.fff = gg
        self.date = datetime.datetime.today()
        self.c = 1 + 2j
        self.g = []
        self.g.append(model2())


class model2(object):
    def __init__(self):
        self.salary = 100.45
        self.new_employee = True


a = model()
# b = unJsonify(jsonify(a))
# print("name = ", b["name"])
# print("salary = ", b["salary"])
# print("model1 = ", b["model1"] )
# print("bo = ", b["bo"])

b = unJsonify(jsonify(a), model())
print("name =", b.name)
print("salary =", b.salary)
