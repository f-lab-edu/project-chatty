from core.state_manager import StateManager
from service.nlu_service import NLUService
from session.session_storage import SessionStorage


class DialogEngine:
    def __init__(self):
        self.nlu_service = NLUService()
        self.state_manger = StateManager()
        self.session_storage = SessionStorage()

    def get_response(self, client_id: str, client_message: str):
        session = self.session_storage.get_session(client_id)
        intents = self.nlu_service.intent_classify(client_message)
        slots = self.nlu_service.slot_classify(client_message)

        response = self.state_manger.get_response(
            session, client_message, intents, slots
        )
        return response
