class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        print("The light is on")
        self.is_on = True

    def turn_off(self):
        print("The light is off")
        self.is_on = False

