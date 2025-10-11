import os
import json
from main.utils.data.data_utils import DataUtils
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class JSONLoader:      
    with open('../../../resources/test_data.json', 'r', encoding='utf-8') as data:
        test_data = DataUtils.dict_to_model(json.loads(data.read()))
        
    with open('../../../resources/API_endpoints.json', 'r', encoding='utf-8') as data:
        API_endpoints = DataUtils.dict_to_model(json.loads(data.read()))