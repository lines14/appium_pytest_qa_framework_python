from config import Config
from main.utils.API.base_API import BaseAPI
from main.utils.data.JSON_loader import JSONLoader

class AuthAPI(BaseAPI):
    def __init__(self, base_URL=None, log_string=None):
        super().__init__(
            log_string, 
            Config().WAIT_TIME,
            base_URL or '' or Config().API_BASE_URL
        )

    def get_temp_user(self, id):
        return super().get(f'{JSONLoader.API_endpoints().auth.temp_users}/{id}')