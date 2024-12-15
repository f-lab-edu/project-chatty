from boxes.base_box import Box, BoxType


class EndBox(Box):
    def __init__(self):
        self.box_type = BoxType.END
