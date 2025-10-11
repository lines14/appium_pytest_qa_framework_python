from config import Config
from main.utils.API.base_API import BaseAPI
from main.utils.data.JSON_loader import JSONLoader

class AuthAPI(BaseAPI):
    def __init__(self, base_URL=None, log_string=None):
        super().__init__(
            base_URL or '' or Config().API_BASE_URL,
            log_string, 
            Config().WAIT_TIME
        )

    async def get_temp_user(self, id):
        return await super().get(f'{JSONLoader.API_endpoints.auth.temp_users}/{id}')