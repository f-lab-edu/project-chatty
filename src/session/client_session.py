import time
from typing import Any, Dict, List, Optional


class Session:
    def __init__(self):
        self.current_state = None
        self.current_intent = None
        self.params: Dict[str, Any] = {}
        self.timestamp = time.time()
        self.expire_time_in_seconds = 60 * 60
        self.intent_history: List[Optional[str]] = []
        self.state_history: List[Optional[str]] = []

    def get_current_intent(self):
        return self.current_intent

    def get_current_state(self):
        return self.current_state

    def set_params(self, key_, value_):
        self.params[key_] = value_

    def set_current_intent(self, intent: str):
        prev_intent = self.current_intent
        self.intent_history.append(prev_intent)
        self.current_intent = intent

    def set_current_state(self, state: str):
        prev_state = self.current_state
        self.state_history.append(prev_state)
        self.current_state = state
