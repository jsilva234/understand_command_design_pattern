class RemoteControl:
    def __init__(
        self,
        turn_on_command,
        turn_off_command,
    ):
        self.turn_on_command = turn_on_command
        self.turn_off_command = turn_off_command

    def turn_on(self):
        self.turn_on_command.execute()

    def turn_off(self):
        self.turn_off_command.execute()


class Calculator:
    def __init__(self):
        self.history = []
        self.undo_stack = []

    def execute(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.undo_stack.append(command)

    def redo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.execute()
            self.history.append(command)
