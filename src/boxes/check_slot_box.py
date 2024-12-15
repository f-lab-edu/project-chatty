from typing import Dict, Union

from boxes.base_box import Box, BoxType
from boxes.base_box import SlotType


class CheckSlotBox(Box):
    def __init__(self, slot_name: str, next: Box = None, fail: Box = None):
        super().__init__(next, fail)
        self.box_type = BoxType.CHECK_SLOT
        self.slot_type = SlotType(slot_name)
