import httpx
from main.utils.log.logger import Logger

class BaseAPI:
    def __init__(self, base_URL, timeout=None, headers=None, log_string=None):
        if log_string: Logger.log(f"{log_string} {base_URL}")
        self.client = httpx.AsyncClient(
            base_url=base_URL, 
            headers=headers, 
            timeout=timeout
        )

    async def get(self, endpoint, params=None):
        Logger.log(f"[req] ▶ get {params or {}} from {endpoint}:")
        response = await self.client.get(endpoint, params=params)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    async def post(self, endpoint, data=None):
        Logger.log(f"[req] ▶ post {data or {}} to {endpoint}:")
        response = await self.client.post(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    async def put(self, endpoint, data=None):
        Logger.log(f"[req] ▶ put {data or {}} to {endpoint}:")
        response = await self.client.put(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    async def patch(self, endpoint, data=None):
        Logger.log(f"[req] ▶ patch {data or {}} to {endpoint}:")
        response = await self.client.patch(endpoint, json=data)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response

    async def delete(self, endpoint):
        Logger.log(f"[req] ▶ delete {endpoint}:")
        response = await self.client.delete(endpoint)
        Logger.log(f"[res]   status code: {response.status_code}")
        if not response.is_success:
            Logger.log(f"[res]   body: {response.text}")
        return response