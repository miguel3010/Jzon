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
    elif(isinstance(model, dict)):
        json = _encode_dict_data(model)
    elif (isClass(model)):
        json = _encode_model_data(model)
    else:
        json = ""

    return str(json)


def _encode_list_data(model):
    b = len(model) > 1
    valid = False
    json = "["
    for item in model:
        if(b and valid):
            json += ","
            valid = False
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
            string = _encode_primitive_data_attribute(model, attribute, value)
            if(string is not None and string != ""):
                json += string
                valid = True
    json += "}"
    return json


def _encode_primitive_data_attribute(a, attribute, value):
    return "\"" + attribute + "\":" + _encode_primitive_data(value)


def _encode_primitive_data(value):
    if(isinstance(value, bool)):
        return str(value).lower()
    elif(isinstance(value, str)):
        return "\"" + value + "\""
    elif(isinstance(value, int)):
        return str(value)
    elif(isinstance(value, float)):
        return str(value)
    elif(isinstance(value, datetime.datetime)):
        return "\"" + str(value.replace(microsecond=0).isoformat('T')) + "\""
    elif(isinstance(value, complex)):
        return "{\"type\":\"complex\",\"real\":" + \
            str(value.real) + ",\"imag\":" + str(value.imag) + "}"
    return "\"\""
