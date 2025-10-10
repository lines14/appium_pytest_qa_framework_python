import json
from main.utils.log.logger import Logger

class DataUtils:
    @staticmethod
    def is_JSON(API_response):
        Logger.log('[info] ▶ check API response is JSON')
        if type(API_response) == list:
            return type(API_response.pop()) == dict
        else:
            return type(API_response) == dict
    
    @staticmethod
    def model_to_dict(model):
        return {key: value for key, value in vars(model).items() if not key.startswith('__')}

    @classmethod
    def nested_data_to_models(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj
    
    @classmethod
    def dict_to_model(cls, dict):
        return json.loads(json.dumps(dict, ensure_ascii=False), object_hook=cls.nested_data_to_models)