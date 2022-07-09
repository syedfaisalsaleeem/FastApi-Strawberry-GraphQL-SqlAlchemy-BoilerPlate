from sqlalchemy.inspection import inspect
import re

def convert_camel_case(name):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', name).lower()
    return name

def get_only_selected_fields(db_baseclass_name,info):
    db_relations_fields = inspect(db_baseclass_name).relationships.keys()
    selected_fields = [convert_camel_case(field.name)  for field in info.selected_fields[0].selections if field.name not in db_relations_fields]
    return selected_fields
    
def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object,column.name)
        except:
            pass
    return data_dict