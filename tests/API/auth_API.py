from config import Config
from main.utils.log.logger import Logger
from main.utils.API.base_API import BaseAPI
from main.utils.data.data_utils import DataUtils
from main.utils.data.JSON_loader import JSONLoader

class AuthAPI(BaseAPI):
    _token = None
    _headers = {}

    def __init__(self, base_URL=None, headers=None):
        self.user = Config().USER
        super().__init__(
            base_URL=base_URL or Config().API_BASE_URL,
            timeout=Config().WAIT_TIME,
            headers=headers or AuthAPI._headers
        )

    async def auth(self, user=None, API_name='Auth API'):
        user = user or self.user
        Logger.log(f'[inf]   login in {API_name} as {user.login}:')
        return await self.post(
            JSONLoader.API_endpoints.auth.login,
            DataUtils.model_to_dict(user)
        )

    async def set_token(self):
        response = await self.auth()
        if response.is_success:
            AuthAPI._token = DataUtils.dict_to_model(response.json()).data.access_token
            AuthAPI._headers = {'Authorization': f'Bearer {AuthAPI._token}'}
            self.client.headers.update(AuthAPI._headers)
        return response

    async def get_temp_user(self, user_id):
        return await self.get(f"{JSONLoader.API_endpoints.auth.temp_users}/{user_id}")