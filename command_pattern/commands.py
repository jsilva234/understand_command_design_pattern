from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightCommand(Command, ABC):
    def __init__(self, light):
        self.light = light


class LightOnCommand(LightCommand):
    def execute(self):
        self.light.turn_on()


class LightOffCommand(LightCommand):
    def execute(self):
        self.light.turn_off()


class UndoableCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AddCommand(UndoableCommand):
    def __init__(self, receiver, number):
        self.receiver = receiver
        self.number = number

    def execute(self):
        self.receiver.add(self.number)

    def undo(self):
        self.receiver.subtract(self.number)
