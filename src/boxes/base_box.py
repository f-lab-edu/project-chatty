from enum import Enum


class Box:
    def __init__(self, next: Box = None, fail: Box = None):
        self.box_type: BoxType
        self.next = next
        self.fail = fail


class BoxType(str, Enum):
    ENTRY = "entry"
    END = "end"
    SYSTEM_UTTER = "system_utterance"
    CLASSIFIY_INTENT = "classifiy_intent"
    CHECK_SLOT = "check_slot"
    ACTION = "action"


class IntentType(str, Enum):
    ORDER = "order"
    INQUIRY = "inquiry"
    REFUND = "refund"


class SlotType(str, Enum):
    ITEM_QUANTITY = "item_quantity"
    ITEM_TYPE = "item_type"


class ActionType(str, Enum):
    ORDER = "order"
    POST_INQUIRY = "post_inquiry"
    REQUEST_REFUND = "request_refund"
