# journal.py
import os
from datetime import datetime

JOURNAL_DIR = "journal"  # Always relative to current dir

class Journal:
    def __init__(self):
        os.makedirs(JOURNAL_DIR, exist_ok=True)
        self.file_path = self._get_current_log_file()
        self.file = open(self.file_path, "a", encoding="utf-8")

    def _get_current_log_file(self):
        now = datetime.now()
        period = "AM" if now.hour < 12 else "PM"
        filename = f"{now.strftime('%Y-%m-%d')}_{period}.log"
        return os.path.join(JOURNAL_DIR, filename)

    def write(self, user_input, response):
        timestamp = datetime.now().strftime("%H:%M")
        self.file.write(f"[{timestamp}] You: {user_input}\n")
        self.file.write(f"[{timestamp}] Soulframe: {response}\n\n")
        self.file.flush()  # Ensure it's written in real-time

    def close(self):
        self.file.close()
