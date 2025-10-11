import json
from typing import Optional
from tests.DB.models import TempUser
from datetime import datetime, timezone

class AuthDB:    
    async def get_temp_user(self, id: int) -> Optional[TempUser]:
        result = await TempUser(**locals()).get()

        if not result:
            return None
        
        return json.dumps(
            result.pop().model_dump(),
            default=lambda prop: (
                prop.astimezone(timezone.utc)
                    .isoformat(timespec='microseconds')
                    .replace('+00:00', 'Z')
                if isinstance(prop, datetime) else str(prop)
            )
        )