import abc
from typing import List

from slot.base_slot import Slot


class Intent(abc.ABC):
    def __init__(self, name: str):
        self.name = name
        self.slots: List[Slot] = []

    def add_slot(self, slot: Slot):
        self.slots.append(slot)
