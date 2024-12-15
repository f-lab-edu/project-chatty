from typing import Any, Dict, Optional

from boxes.base_box import Box, BoxType
from scenarios.base_scenario import Scenario
from scenarios.order import OrderScenario
from session.client_session import Session


class StateMachine:
    def __init__(self):
        self.intent_scenario_mapping: Dict[str, Scenario] = {}
        self.set_statemachine()

    def set_statemachine(self):
        self.intent_scenario_mapping["order"] = OrderScenario()

    def get_response(
        self, session: Session, classified_intent: str, slots: Dict[str, Any]
    ) -> str:
        cur_state = self.check_current_state(session, classified_intent)
        response = self.change_state(session, cur_state, slots)
        return response

    def check_current_state(self, session: Session, classified_intent: Optional[str]) -> Box:
        cur_intent = session.get_current_intent()
        is_entry = self.check_is_entry(classified_intent, cur_intent)

        if is_entry:
            cur_intent = "entry"
            cur_state = self.intent_scenario_mapping[cur_intent].start_state
            return cur_state

        if classified_intent is not None and classified_intent != cur_intent:
            cur_state = self.intent_scenario_mapping[classified_intent].start_state
            return cur_state

        cur_state_key = session.get_current_state_key()
        cur_state = self.intent_scenario_mapping[cur_intent].get_state(cur_state_key)
        return cur_state


    def process_state(self,cur_state: Box, ):


    def change_state(self, session: Session, cur_state, slots):
        while True:
            if cur_state.box_type == "classify_intent":
                cur_state = cur_state.next
            elif cur_state.box_type == "check_slot":
                if cur_state.slot_type.value in slots:
                    slot_type = cur_state.slot_type.value
                    session.set_params(slot_type, slots[slot_type])
                    cur_state = cur_state.next
                else:
                    response = f"please input {cur_state.slot_type.value}"
                    session.current_state = cur_state
                    break
                    # retry 횟수 증가
            elif cur_state.box_type == "action":
                # API Gateway
                response = f"{cur_state.action_type.value} Done"
                session.current_state = None
                break
        return response

    def check_is_entry(self, classified_intent: Optional[str], cur_intent: Optional[str]) -> bool:
        if classified_intent is None:
            if cur_intent is None:
                return True
            return False
        if classified_intent == BoxType.ENTRY:
            return True
        return False
