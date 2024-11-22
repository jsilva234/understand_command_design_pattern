from command_pattern.commands import LightOnCommand, LightOffCommand
from command_pattern.invokers import RemoteControl
from command_pattern.receivers import Light


if __name__ == '__main__':
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    remote = RemoteControl(light_on_command, light_off_command)
    remote.turn_on()  # Output: "The light is on"
    remote.turn_off()  # Output: "The light is off"
