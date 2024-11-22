class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        print("The light is on")
        self.is_on = True

    def turn_off(self):
        print("The light is off")
        self.is_on = False


class Number:
    def __init__(self, initial_value):
        self.state = initial_value

    def add(self, value):
        self.state += value
        print(f"Adding: {value}")

    def subtract(self, value):
        self.state -= value
        print(f"Subtracting: {value}")

    def __repr__(self):
        return str(self.state)
