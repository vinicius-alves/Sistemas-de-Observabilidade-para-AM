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

    for key in dir(obj):
        if key.startswith("__"): 
            continue
        try:
            value = getattr(obj, key)
        except AttributeError:
            print('error - ',key, value)  
        value_dto = value
        if value.__class__.__module__.startswith('Core.Relations'):
            value_dto = converter_objeto_para_dto(value)

        
        if type(value) == list:
            if not(hasattr(obj_dto, key)):
                setattr(obj_dto, key, [])
            for item in value:
                item_dto = converter_objeto_para_dto(item)
                getattr(obj_dto, key).append(item_dto)           
        else:
            setattr(obj_dto, key, value_dto)
        

    return obj_dto
