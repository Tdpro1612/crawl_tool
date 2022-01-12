from source.body_crawler import *

def get_data(variable,many=False,type=None):
    data=[]
    if type is None:
        if many is True:
            for i in variable:
                data.append(i.text)
        else:
            data.append(variable.text)
    else:
        if many is True:
            for i in variable:
                value=i.get_attribute(type)
                data.append(value)
        else:
            value=variable.get_attribute(type)
            data.append(value)

    return data

def save_data(data):
    pass
    return save_data