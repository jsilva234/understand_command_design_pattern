from command_pattern.commands import AddCommand, LightOffCommand, LightOnCommand
from command_pattern.invokers import Calculator, RemoteControl
from command_pattern.receivers import Light, Number

if __name__ == "__main__":
    # base, simple example
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    remote = RemoteControl(light_on_command, light_off_command)
    remote.turn_on()  # Output: "The light is on"
    remote.turn_off()  # Output: "The light is off"

    # Example with history
    calculator = Calculator()  # invoker
    number = Number(100)

    # add 10
    add_10 = AddCommand(number, 10)
    calculator.execute(add_10)
    print(number)  # 110

    add_20 = AddCommand(number, 20)
    calculator.execute(add_20)
    print(number)  # 130

    calculator.undo()
    print(number)  # 110

    calculator.redo()
    print(number)  # 130
