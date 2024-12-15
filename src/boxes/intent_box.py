from base_box import Box
from base_box import BoxType
from base_box import IntentType
from boxes.check_slot_box import CheckSlot


class IntentBox(Box):
    def __init__(self, intent_name: str, next: Box = None, fail: Box = None):
        super().__init__(next, fail)
        self.box_type = BoxType.CLASSIFIY_INTENT
        self.intent_type = IntentType(intent_name)

    def __repr__(self):
        return f"I-{self.intent_type.value}"
