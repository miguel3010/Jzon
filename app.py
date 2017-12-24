import datetime
import json

from Jzon import jsonify


class model(object):
    def __init__(self):
        self.id = 0
        self.name = "Miguel Ángel Campos"
        self.salary = 100.45
        self.model1 = model2()
        self.bo = True
        self.bod = 'f'
        self.date = datetime.datetime.today()
        self.c = 1 + 2j
        self.g = []
        self.g.append(model2())

class model2(object):
    def __init__(self):
        self.salary = 100.45
        self.new_employee = True


a = model()
print(jsonify(a))
