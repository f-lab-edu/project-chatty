from abc import ABC

from boxes.check_slot_box import CheckSlotBox
from boxes.intent_box import IntentBox
from boxes.action_box import ActionBox
from scenarios.base_scenario import Scenario


class OrderScenario(Scenario):
    def __init__(self):
        self.build_scenario()

    def build_scenario(self):
        intent_order = IntentBox(intent_name="order")
        check_slot_item_type = CheckSlotBox(slot_name="item_type")
        check_slot_item_quantity = CheckSlotBox(slot_name="item_quantity")
        action_order = ActionBox(
            action_name="order", params={"item_type", "item_quantity"}
        )

        intent_order.next = check_slot_item_type
        check_slot_item_type.next = check_slot_item_quantity
        check_slot_item_type.fail = check_slot_item_type
        check_slot_item_quantity.next = action_order
        check_slot_item_quantity.fail = check_slot_item_quantity

        self.states["intent_order"] = intent_order
        self.states["check_slot_item_type"] = check_slot_item_type
        self.states["check_slot_item_quantity"] = check_slot_item_quantity
        self.states["action_order"] = action_order

    def get_state(self, state_name: str):
        return self.stattes[state_name]

    @property
    def start_state(self):
        return self.intent_order
