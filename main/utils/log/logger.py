import os
from datetime import datetime

class Logger:
    _logs = []

    @staticmethod
    def log(step: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        decoded_step = Logger._safe_decode(step)
        print(f"\n{decoded_step}")
        Logger._logs.append((timestamp, decoded_step))

    @staticmethod
    def log_to_file(filename: str = "../../../artifacts/log.txt"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a", encoding="utf-8") as file:
            for timestamp, message in Logger._logs:
                file.write(f"{timestamp}  {message}\n")

    @staticmethod
    def get_timings():
        return [timestamp for timestamp, message in Logger._logs]

    @staticmethod
    def _safe_decode(text: str) -> str:
        if "\\u" in text:
            try:
                return text.encode("utf-8").decode("unicode_escape")
            except Exception:
                return text
        return text