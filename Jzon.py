import datetime
import types

# ENCODING


def isClass(model):
    if(isinstance(model, object)):
        return not(isinstance(model, bool)
                   or isinstance(model, str)
                   or isinstance(model, int)
                   or isinstance(model, float)
                   or isinstance(model, complex)
                   or isinstance(model, datetime.datetime)
                   or isinstance(model, dict)
                   or isinstance(model, list))
    return False


def jsonify(model):
    json = ""
    if(isinstance(model, list)):
        json = _encode_list_data(model)
    if(isinstance(model, dict)):
        json =  _encode_dict_data(model)
    elif (isClass(model)):
        json =  _encode_model_data(model)
    else:
        json =  ""
    
    return str(json)
     

def _encode_list_data(model):
    json = "["
    for item in model:
        if(isinstance(item, dict)):
            string = _encode_dict_data(item)
            if(string is None or string == ""):
                string = "{}"
            json += string
            valid = True
        elif (isClass(item)):
            string = _encode_model_data(item)
            if(string is None or string == ""):
                string = "{}"
            json += string
            valid = True
        elif(isinstance(item, list)):
            string = _encode_list_data(item)
            if(string is None or string == ""):
                string = "[]"
            json += string
            valid = True
        else:
            string = _encode_primitive_data(item)
            if(string is not None and string != ""):
                json += string
                valid = True
    json += "]"
    return json


def _encode_model_data(model: object):
    items = model.__dict__.items()
    return _raw_model_encode(model, items)


def _encode_dict_data(model: dict):
    items = model.items()
    return _raw_model_encode(model, items)


def _raw_model_encode(model, items):
    b = len(items) > 1
    valid = False
    json = "{"
    for attribute, value in items:
        if(b and valid):
            json += ","
            valid = False
        attr = getattr(model, attribute)
        if(isinstance(attr, dict)):
            string = _encode_dict_data(attr)
            if(string is None or string == ""):
                string = "{}"
            json += "\"" + attribute + "\":" + string
            valid = True
        elif (isClass(attr)):
            string = _encode_model_data(attr)
            if(string is None or string == ""):
                string = "{}"
            json += "\"" + attribute + "\":" + string
            valid = True
        elif(isinstance(attr, list)):
            string = _encode_list_data(attr)
            if(string is None or string == ""):
                string = "[]"
            json += "\"" + attribute + "\":" + string
            valid = True
        else:
            string = _encode_primitive_data(model, attribute, value)
            if(string is not None and string != ""):
                json += string
                valid = True
    json += "}"
    return json


def _encode_primitive_data(a, attribute, value):
    json = ""
    if(type(getattr(a, attribute)) == bool):
        print(attribute + " = bool")
        json += "\"" + attribute + "\":\"" + str(value).lower() + "\""
        valid = True
    elif(isinstance(getattr(a, attribute), str)):
        print(attribute + " = String")
        json += "\"" + attribute + "\":\"" + value + "\""
        valid = True
    elif(isinstance(getattr(a, attribute), int)):
        print(attribute + " = integer")
        json += "\"" + attribute + "\":" + str(value)
        valid = True
    elif(isinstance(getattr(a, attribute), float)):
        print(attribute + " = float")
        json += "\"" + attribute + "\":" + str(value)
        valid = True
    elif(isinstance(getattr(a, attribute), datetime.datetime)):
        print(attribute + " = datetime")
        json += "\"" + attribute + "\":\"" + \
            str(value.replace(microsecond=0).isoformat('T')) + "\""
        valid = True
    elif(isinstance(getattr(a, attribute), complex)):
        print(attribute + " = datetime")
        json += "\"" + attribute + \
            "\":{\"type\":\"complex\",\"real\":" + \
                str(value.real) + ",\"imag\":" + str(value.imag) + "}"
        valid = True

    return json
