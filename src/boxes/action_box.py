from typing import Set

from boxes.base_box import Box
from boxes.base_box import BoxType
from boxes.base_box import ActionType


class ActionBox(Box):
    def __init__(self, action_name: str, params: Set):
        self.box_type = BoxType.ACTION
        self.action_type = ActionType(action_name)
        self.params = params
