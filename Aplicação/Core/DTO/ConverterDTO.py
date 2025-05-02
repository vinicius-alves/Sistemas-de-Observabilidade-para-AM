import importlib

class ConverterDTO:

    def __init__(self, session):
        self.session = session

    def get_dto_prototype(self,obj):
        base_class = obj.__class__.__bases__[0]
        if base_class != object:
            name_class_base = base_class.__name__
        else:
            name_class_base = obj.__class__.__name__
        
        name_class=name_class_base +'DTO'
        module = importlib.import_module('Core.DTO.'+name_class)

        class_inst = getattr(module, name_class)
        obj_dto_prototype = class_inst()  

        name_class_repo=name_class_base +'Repository'
        class_inst = getattr(module, name_class_repo)
        repo = class_inst(session = self.session)

        return obj_dto_prototype, repo

    def converter_object_to_dto(self, obj):

        if not(obj.__class__.__module__.startswith('Core.Relations')):
            return obj
        
        item_exists, obj_dto = self.get_if_exists( obj )
        if item_exists:
            return obj_dto

        obj_dto_prototype, repo = self.get_dto_prototype(obj)
        
        for key in dir(obj):
            if key.startswith("__"): 
                continue
            try:
                value = getattr(obj, key)
            except AttributeError:
                print('error - ',key, value)    
            
            if value is None:
                continue

            value_dto = value
            if value.__class__.__module__.startswith('Core.Relations'):
                value_dto = self.converter_object_to_dto(value)
            
            if type(value) == list:
                if not(hasattr(obj_dto_prototype, key)):
                    setattr(obj_dto_prototype, key, [])
                for item in value:
                    item_dto = self.converter_object_to_dto(item)
                    getattr(obj_dto_prototype, key).append(item_dto)           
            else:
                setattr(obj_dto_prototype, key, value_dto)

        
            
        return obj_dto_prototype

    def get_if_exists(self, obj):

        obj_dto_prototype, repo = self.get_dto_prototype(obj)

        primary_key = obj_dto_prototype.__mapper__.primary_key[0].name
        item_id =  getattr(obj, primary_key, None) 

        if item_id is not None:
            existing_item = repo.get(item_id)
            if existing_item:
                return True, existing_item
          
        if hasattr(obj_dto_prototype, 'get_secondary_key'):
            lst_secondary_key = obj_dto_prototype.get_secondary_key()
            dict_search = {}
            if not(type(lst_secondary_key) == list):
                return False, obj_dto_prototype

            for key in lst_secondary_key:
                item_id =  getattr(obj, key, None) 
                if item_id is None:
                    return False, obj_dto_prototype
                dict_search[key] = item_id
            
            existing_item = repo.filter_by(dict_search).first()
            if existing_item:
                return True, existing_item
            
        return False, obj_dto_prototype

