import abc


class Scenario(abc.ABC):
    @abc.abstractmethod
    def build_scenario(self):
        pass
