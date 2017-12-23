import datetime
import json

from Jzon import jsonify


class model(object):
    def __init__(self):
        self.id = 0
        self.name = ""
        self.salary = 100.45
        self.model1 = model2()
        self.bo = True
        self.bod = 'f'
        self.date = datetime.datetime.today()
        self.c = 1 + 2j
        self.g = []
        self.g.append(model2())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)  

class model2(object):
    def __init__(self):
        self.salary = 100.45
        self.bo = True


a = model()
print(jsonify(a)) 