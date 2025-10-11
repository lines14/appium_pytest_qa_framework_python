import json
from assertions import assert_json

class DataUtils:
    @staticmethod
    def is_JSON(API_response):
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
    
    def assert_json(actual: dict, expected: dict, excluded_fields=None):
        excluded_fields = set(excluded_fields or [])

        def _filter(data):
            return {key: value for key, value in data.items() if key not in excluded_fields}

        actual_filtered = _filter(actual)
        expected_filtered = _filter(expected)
        assert_json(actual_filtered, expected_filtered)