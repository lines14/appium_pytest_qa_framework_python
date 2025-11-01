import json
from typing import Optional
from datetime import datetime
from tests.DB.models import TempUser
from main.utils.time.time_utils import TimeUtils

class AuthDB:    
    async def get_temp_user(self, id: int) -> Optional[str]:
        result = await TempUser(**locals()).get()

        if not result:
            return None
        
        return json.dumps(
            result.pop().model_dump(),
            default=lambda prop: (
                TimeUtils.to_UTC(prop).isoformat(timespec='microseconds').replace('+00:00', 'Z')
                if isinstance(prop, datetime) else str(prop)
            )
        )