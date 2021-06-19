# fasaad design pattern py file

# facade class
class ComplexCoffeMachine():
    """ Complex Coffee Machine Facade class. It calls other complex classes. """

    def __init__(self):
        """ initialization """

        self.grinder = _Grinder()
        self.kettle = _Kettle()
        self.pressure = _PressureUnit()
        self.distiller = _Distiller()
        self.water_tank = 0
        self.coffee_tank = 0

    def add_water(self, amount_of_water):
        """ Add Water to water tank. """
        self.water_tank = self.water_tank + amount_of_water

    def get_amount_of_water(self):
        """ Get amount of water of water tank. """
        return self.water_tank

    def add_coffee_beans(self, amount_of_coffee):
        """ Add coffee beans to coffee tank. """
        self.coffee_tank = self.coffee_tank + amount_of_coffee

    def get_amount_coffee_beans(self):
        """ Get amount of coffee beans. """
        return self.coffee_tank

    def make_filter_coffee(self, cup_count):
        """ Make Filter Coffee """
        water = cup_count * 250
        coffee = cup_count * 12
        self.grinder.change_coffee_bean_size(4)
        ground_coffee = self.grinder.grind_coffee(coffee)
        temp_water = self.kettle.boil_water(water, 94)
        self.distiller.distill(ground_coffee, temp_water)

        print(f"Filter Coffee Is ready for {cup_count} cups.")


class _Grinder():
    """ Grinder Unit Class """

    def __init__(self):
        """ initialization """
        self.turn_per_second = 30
        self.coffe_bean_size = 4

    def change_turn_per_second(self, turn_count):
        """ Change the blades turn count. max 10-30 """
        self.turn_per_second = turn_count

    def change_coffee_bean_size(self, bean_size):
        """ Change the coffee bean size. 1-10 """
        self.coffe_bean_size = bean_size

    def grind_coffee(self, amount_of_coffee):
        """ Start the coffee grinder. 30gr coffee bean -> 15sec. """
        time = (amount_of_coffee * self.coffe_bean_size / self.turn_per_second) * 1.8
        print(f"Coffee Grind Operation Completed! It tooks {time} seconds")

        return amount_of_coffee


class _Kettle():
    """ Kettle Unit Class """

    def __init__(self):
        """ initialization """
        self.amount_of_water = 0

    def boil_water(self, amount_of_water, tempature):
        """ Boil water to desired tempature. """
        time = (tempature * amount_of_water) / 450
        print(f"Water is ready! It tooks {time} seconds. ")
        return (amount_of_water * 98) / 100


class _PressureUnit():
    """ Pressure Unit Class """

    def __init__(self):
        """ initialization """


class _Distiller():
    """ Pressure Unit Class """

    def __init__(self):
        pass

    def distill(self, coffee, water):
        """ Distill coffee """
        time = 150 + (coffee * water) / 200
        print(f"Distill Operation Completed! It tooks {time} seconds.")


def main():
    """ Main Function Of Facade. It is client of Facade Pattern. """

    hikmet_bey = ComplexCoffeMachine()
    hikmet_bey.add_coffee_beans(1000)
    hikmet_bey.add_water(2000)
    hikmet_bey.make_filter_coffee(3)

if __name__ == "__main__":
    main()