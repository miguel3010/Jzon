import datetime
import types
import json 

# ENCODING


def isClass(model):
    if(model is None):
        return False

    if(isinstance(model, object)):
        if(isinstance(model, datetime.datetime)
                or isinstance(model, datetime.date)):
            return False

        return not(isinstance(model, bool)
                   or isinstance(model, str)
                   or isinstance(model, int)
                   or isinstance(model, float)
                   or isinstance(model, complex)
                   or isinstance(model, dict)
                   or isinstance(model, list))
    return False


def jsonify(model):
    """
    Serialization of an object class, dict or list into JSON format

    Arguments:
        model {class object, dict or list} -- The model to be serialized

    Returns:
        [string] -- JSON Formatted string of the model
    """

    if(model is None):
        return "null"

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
        attr = None
        try:
            attr = getattr(model, attribute)
        except Exception:
            pass

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
    if(value is None):
        return "null"
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
    elif(isinstance(value,datetime.date)):        
        f = datetime.datetime.combine(value, datetime.time.min)
        return _encode_primitive_data(f)
    elif(isinstance(value, complex)):
        return "{\"type\":\"complex\",\"real\":" + str(value.real) + ",\"imag\":" + str(value.imag) + "}"
    return "\"\""

# DECODING


def unJsonify(json_, typed=None):
    """
    Deserialization of an object class, dict or list into Python Object class or dict

    Arguments:
        json_ {JSON formatted text} -- The text to be deserialized
        typed(default = dict)   --      The class type that apply to the Python class
    Returns:
        [type(typed)] -- dict if arg [typed] is None
    """

    if(typed is None):
        return unJsonify(json_, {})

    if(isinstance(typed, dict)):
        return json.loads(json_)
    elif (isClass(typed)):
        dict_ = unJsonify(json_)
        for key, value in dict_.items():
            if(isClass(getattr(typed, key))):
                setattr(typed, key, _parseModel(typed, key, value))
            else:
                try:
                    setattr(typed, key, value)
                except Exception:
                    pass
        return typed


def parse_from_dict(typed, model):
    dict_ = model
    for key, value in dict_.items():
        try:
            if(isClass(getattr(typed, key))):
                setattr(typed, key, _parseModel(typed, key, value))
            else:
                try:
                    setattr(typed, key, value)
                except Exception:
                    pass
        except Exception:
            pass
    return typed


def _parseModel(typed, key, value):
    clas = getattr(typed, key).__class__
    m = clas.__module__
    module = __import__(m, globals(), locals(), ['object'], 0)
    class_ = getattr(module, clas.__name__)
    instance = class_()
    instance = parse_from_dict(instance, value)
    return instance
