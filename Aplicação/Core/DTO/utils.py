import importlib

def converter_objeto_para_dto(obj : object):
    base_class = obj.__class__.__bases__[0]
    if base_class != object:
        name_class = base_class.__name__
    else:
        name_class = obj.__class__.__name__

    name_class+='DTO'

    module = importlib.import_module('Core.DTO.'+name_class)
    Classe = getattr(module, name_class)
    obj_dto = Classe()  

    for key, value in obj.__dict__.items():
        value_dto = value
        if value.__class__.__module__.startswith('Core.Relations'):
            value_dto = converter_objeto_para_dto(value)
        obj_dto.__dict__[key] = value_dto

        if type(value) == list:
            lst_value_dto =[]
            for item in value:
                item_dto = converter_objeto_para_dto(item)
                lst_value_dto.append(item_dto)
            obj_dto.__dict__[key] = lst_value_dto

    return obj_dto
