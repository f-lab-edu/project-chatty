from boxes.base_box import Box, BoxType
from boxes.system_uttr_box import SystemUtter


class EntryBox(Box):
    def __init__(self):
        self.box_type = BoxType.ENTRY
