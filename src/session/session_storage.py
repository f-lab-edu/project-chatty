from typing import Dict

from session.client_session import Session


class SessionStorage:
    def __init__(self):
        self.client_sessions: Dict[str, Session] = {}

    def get_or_create_session(self, client_id):
        if client_id not in self.client_sessions:
            self.client_sessions[client_id] = Session()
        return self.client_sessions[client_id]
