# memory.py

class MemoryBuffer:
    def __init__(self, enabled=False, max_messages=20):
        self.enabled = enabled
        self.max_messages = max_messages
        self.messages = []

    def add(self, role, content):
        if not self.enabled:
            return
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get(self):
        return self.messages if self.enabled else []

    def reset(self):
        self.messages = []
