from boxes.base_box import Box, BoxType


class SystemUtterBox(Box):
    def __init__(self, utterance: str):
        self.box_type = BoxType.SYSTEM_UTTER
        self.utterance = utterance
