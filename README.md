# Jzon
Python3 library for serialization and deserialization of python objects/dicts

## Usage
Encode
```
from Jzon import jsonify
print(jsonify(a)) # a is a Class object, dict, or list
```

```
import datetime
from Jzon import jsonify
class model(object):
    def __init__(self):
        self.id = 30
        self.name = "Miguel Angel Campos"
        self.height = 1.80
        self.intExample = 45
        self.boolExample = True
        self.model2 = model2()
        self.sex = "M"
        self.date = datetime.datetime.today()
        self.complexN = 1 + 2j
        self.arrayExample = []
        self.arrayExample.append(model2())

class model2(object):
    def __init__(self):
        self.salary = 100.45
        self.bo = True


a = model()
print(jsonify(a))
>>>{"boolExample":"true","arrayExample":[{"salary":100.45,"bo":"true"}],"complexN":{"type":"complex","real":1.0,"imag":2.0},"name":"Miguel Angel Campos","id":30,"sex":"M","model2":{"salary":100.45,"bo":"true"},"intExample":45,"height":1.8,"date":"2017-12-23T14:53:42"}
```

## Authors
* **Miguel Ángel Campos** - *Software Engineer* - [Linkedin](https://www.linkedin.com/in/miguel-angelcampos)
