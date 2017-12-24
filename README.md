# Jzon
Python3 library for serialization and deserialization of python objects/dicts

## Usage
####Encode
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
#### Decode
```
from Jzon import unJsonify 
print(unJsonify(JSON_TXT)) # JSON_TXT is a JSON Formatted Text
```
```
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

modelresponse = unJsonify(jsonify(a), model())
```
#### Parsing
Convert dict to python class object (if apply).
```
parse_from_dict(model(),_dict) # model() is the object with desired type, _dict is the dictionary corresponding to model
```

## Authors
* **Miguel Ángel Campos** - *Software Engineer* - [Linkedin](https://www.linkedin.com/in/miguel-angelcampos)
