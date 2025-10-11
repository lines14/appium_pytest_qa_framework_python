import httpx
from main.utils.log.logger import Logger

class BaseAPI:
    def __init__(self, base_URL, log_string, timeout=None, headers=None):
        Logger.log(f"{log_string or '[info] ▶ set base API URL'} {base_URL}")
        self.__client = httpx.AsyncClient(
            base_url=base_URL,
            headers=headers,
            timeout=timeout
        )

    async def get(self, endpoint, params=None):
        Logger.log(f'[info] ▶ get {params} from {endpoint}:')
        response = await self.__client.get(url=endpoint, params=params)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    async def post(self, endpoint, data=None):
        Logger.log(f'[info] ▶ post {data} to {endpoint}:')
        response = await self.__client.post(url=endpoint, data=data)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    async def put(self, endpoint, data=None):
        Logger.log(f'[info] ▶ put {data} to {endpoint}')
        response = await self.__client.put(url=endpoint, data=data)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    async def patch(self, endpoint, data=None):
        Logger.log(f'[info] ▶ patch {data} to {endpoint}')
        response = await self.__client.patch(url=endpoint, data=data)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response

    async def delete(self, endpoint):
        Logger.log(f'[info] ▶ delete {endpoint}')
        response = await self.__client.delete(url=endpoint)
        Logger.log(f'[info]   status code: {response.status_code}')
        return response