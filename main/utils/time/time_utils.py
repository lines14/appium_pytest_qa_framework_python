from datetime import datetime, timezone, timedelta
from main.utils.data.JSON_loader import JSONLoader

class TimeUtils:
    @staticmethod
    def to_UTC(dt: datetime) -> datetime:
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone(timedelta(hours=JSONLoader.config_data.time_delta)))

        return dt.astimezone(timezone.utc)