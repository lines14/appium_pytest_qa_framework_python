import os
import json
from main.utils.data.data_utils import DataUtils
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class JSONLoader:      
    @property
    def test_data(self):
        with open('../../../resources/test_data.json', 'r', encoding='utf-8') as data:
            return DataUtils.dict_to_model(json.loads(data.read()))
        
    @property
    def API_endpoints(self):
        with open('../../../resources/API_endpoints.json', 'r', encoding='utf-8') as data:
            return DataUtils.dict_to_model(json.loads(data.read()))