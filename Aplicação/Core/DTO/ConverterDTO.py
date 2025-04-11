import importlib

class ConverterDTO:

    def __init__(self, session):
        self.session = session

    def get_dto_obj(self,obj):
        base_class = obj.__class__.__bases__[0]
        if base_class != object:
            name_class_base = base_class.__name__
        else:
            name_class_base = obj.__class__.__name__
        
        name_class=name_class_base +'DTO'
        module = importlib.import_module('Core.DTO.'+name_class)

        class_inst = getattr(module, name_class)
        obj_dto = class_inst()  

        name_class_repo=name_class_base +'Repository'
        class_inst = getattr(module, name_class_repo)
        repo = class_inst(session = self.session)

        return obj_dto, repo

    def converter_object_to_dto(self, obj):
        obj_dto, repo = self.get_dto_obj(obj)
        
        for key in dir(obj):
            if key.startswith("__"): 
                continue
            try:
                value = getattr(obj, key)
            except AttributeError:
                print('error - ',key, value)  
            value_dto = value
            if value.__class__.__module__.startswith('Core.Relations'):
                value_dto = self.converter_object_to_dto(value)
            
            if type(value) == list:
                if not(hasattr(obj_dto, key)):
                    setattr(obj_dto, key, [])
                for item in value:
                    item_dto = self.converter_object_to_dto(item)
                    getattr(obj_dto, key).append(item_dto)           
            else:
                setattr(obj_dto, key, value_dto)

        item_exists, obj_dto = self.get_if_exists( obj_dto, repo)

        if item_exists:
            return obj_dto
            
        return obj_dto

    def get_if_exists(self, obj_dto, repo):

        primary_key = obj_dto.__mapper__.primary_key[0].name
        item_id =  getattr(obj_dto, primary_key, None)

        if item_id is not None:
            existing_item = repo.get(item_id)
            if existing_item:
                return True, existing_item
          
        if hasattr(obj_dto, 'get_secondary_key'):
            secondary_key = obj_dto.get_secondary_key()
            item_id =  getattr(obj_dto, secondary_key, None)

            if item_id is not None:
                existing_item = repo.filter_by({secondary_key: item_id}).first()
                if existing_item:
                    return True, existing_item

            
        return False, obj_dto
