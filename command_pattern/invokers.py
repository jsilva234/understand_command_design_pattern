class RemoteControl:
    def __init__(self, turn_on_command, turn_off_command,):
        self.turn_on_command = turn_on_command
        self.turn_off_command = turn_off_command


    def turn_on(self):
        self.turn_on_command.execute()


    def turn_off(self):
        self.turn_off_command.execute()
