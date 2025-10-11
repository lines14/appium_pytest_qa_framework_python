import json
from typing import Optional
from models import TempUser

class AuthDB:    
    async def get_temp_user(self, search_by: dict) -> Optional[TempUser]:
        result = await TempUser(**search_by).get()

        if not result:
            return None
        
        temp_user = result.pop()
        stringified_temp_user = json.dumps(temp_user.model_dump(), default=str)

        return TempUser(**json.loads(stringified_temp_user))